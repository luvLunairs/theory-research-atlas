"""Check that page refresh is opt-in, validated first and stops on failure."""
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
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


if __name__ == '__main__':
    unittest.main()
