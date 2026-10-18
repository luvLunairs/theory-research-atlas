"""Evaluate the JSON Schema subset used by atlas records, failing on unknown keywords."""
import datetime as dt
import json
import math
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
KEYWORDS={'$schema','$ref','title','description','type','const','enum','properties','required','additionalProperties',
          'items','minItems','uniqueItems','minLength','minimum','pattern','format'}
def read(path): return json.loads(path.read_text(encoding='utf-8'))

def schema_check(value, schema, where, errors, schema_dir=None):
    schema_dir=schema_dir or ROOT/'schemas'
    unsupported=set(schema)-KEYWORDS
    if unsupported:
        errors.append(f'{where}: unsupported schema keywords {sorted(unsupported)}'); return
    if '$ref' in schema:
        ref=schema['$ref']
        if Path(ref).name != ref:
            errors.append(f'{where}: schema references must be sibling files'); return
        schema_check(value,read(schema_dir/ref),where,errors,schema_dir); return
    kinds={'string':lambda x:isinstance(x,str),'array':lambda x:isinstance(x,list),'object':lambda x:isinstance(x,dict),
        'boolean':lambda x:type(x) is bool,'integer':lambda x:type(x) is int,'number':lambda x:type(x) in (int,float),'null':lambda x:x is None}
    types=schema.get('type')
    if types and not any(kinds[t](value) for t in ([types] if isinstance(types,str) else types)):
        errors.append(f'{where}: expected {types}, got {type(value).__name__}'); return
    if type(value) is float and not math.isfinite(value):
        errors.append(f'{where}: number must be finite'); return
    if 'const' in schema and (value!=schema['const'] or type(value) is not type(schema['const'])):
        errors.append(f'{where}: expected constant {schema["const"]!r}')
    if 'enum' in schema and value not in schema['enum']: errors.append(f'{where}: invalid vocabulary value {value!r}')
    if isinstance(value,dict):
        props=schema.get('properties',{})
        for k in schema.get('required',[]):
            if k not in value: errors.append(f'{where}: missing {k}')
        if schema.get('additionalProperties') is False:
            for k in value.keys()-props.keys(): errors.append(f'{where}: unknown field {k}')
        for k,v in value.items():
            if k in props: schema_check(v,props[k],f'{where}.{k}',errors,schema_dir)
    if isinstance(value,list):
        if len(value)<schema.get('minItems',0): errors.append(f'{where}: too few entries')
        if schema.get('uniqueItems') and len({json.dumps(x,sort_keys=True) for x in value})!=len(value): errors.append(f'{where}: duplicate entries')
        for i,x in enumerate(value): schema_check(x,schema.get('items',{}),f'{where}[{i}]',errors,schema_dir)
    if isinstance(value,str):
        if len(value.strip())<schema.get('minLength',0): errors.append(f'{where}: empty text')
        if 'pattern' in schema and not re.search(schema['pattern'],value): errors.append(f'{where}: pattern mismatch')
        try:
            if schema.get('format')=='date':
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value): raise ValueError('date must be YYYY-MM-DD')
                dt.date.fromisoformat(value)
            if schema.get('format')=='date-time':
                parsed=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
                if parsed.tzinfo is None: raise ValueError('timestamp needs timezone')
            if schema.get('format')=='uri':
                p=urlparse(value)
                if p.scheme not in ('http','https') or not p.netloc: raise ValueError('expected HTTP(S) URL')
        except ValueError as exc: errors.append(f'{where}: {exc}')
    if type(value) in (int,float) and value<schema.get('minimum',float('-inf')): errors.append(f'{where}: below minimum')

