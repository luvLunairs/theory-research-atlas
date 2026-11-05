"""Check that page refresh is opt-in, validated first and stops on failure."""
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import unittest

import check


class CheckWorkflowTests(unittest.TestCase):
    def run_workflow(self, arguments, outcomes):
        with patch.object(check.subprocess, 'run',
                          side_effect=[SimpleNamespace(returncode=code) for code in outcomes]) as run:
            with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                result = check.main(arguments)
        return result, [call.args[0][1:] for call in run.call_args_list]

    def test_default_never_refreshes_pages(self):
        result, commands = self.run_workflow([], [0] * 4)
        self.assertEqual(result, 0)
        self.assertEqual(commands, [arguments for _, arguments in check.CHECKS])
        self.assertNotIn(('scripts/render.py',), commands)

    def test_refresh_follows_validation_and_keeps_all_checks(self):
        result, commands = self.run_workflow(['--render'], [0] * 5)
        self.assertEqual(result, 0)
        self.assertEqual(commands[:2], [('scripts/validate.py',), ('scripts/render.py',)])
        self.assertEqual(commands[2:], [arguments for _, arguments in check.CHECKS[1:]])

    def test_invalid_data_prevents_any_refresh(self):
        result, commands = self.run_workflow(['--render'], [2])
        self.assertEqual(result, 2)
        self.assertEqual(commands, [('scripts/validate.py',)])

    def test_failed_refresh_stops_before_other_checks(self):
        result, commands = self.run_workflow(['--render'], [0, 3])
        self.assertEqual(result, 3)
        self.assertEqual(commands, [('scripts/validate.py',), ('scripts/render.py',)])

    def test_children_share_writable_workspace_temp_directory(self):
        directories = []

        def run_child(command, *, cwd, env):
            temporary = Path(env['TMP'])
            self.assertEqual(env['TEMP'], str(temporary))
            self.assertEqual(env['TMPDIR'], str(temporary))
            self.assertTrue(temporary.is_relative_to(check.ROOT / 'work'))
            (temporary / 'child-output.txt').write_text('Temporary check output.', encoding='utf-8')
            directories.append(temporary)
            return SimpleNamespace(returncode=0)

        with patch.object(check.subprocess, 'run', side_effect=run_child):
            with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                self.assertEqual(check.main([]), 0)
        self.assertEqual(len(directories), len(check.CHECKS))
        self.assertEqual(len(set(directories)), 1)
        self.assertFalse(directories[0].exists())


if __name__ == '__main__':
    unittest.main()
