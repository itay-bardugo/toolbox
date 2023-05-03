from typing import Any, Type
from unittest import TestCase

from libs.core.entrypoints.base_entrypoint import Entrypoint


class TestEntrypoint(TestCase):
    def test_integration(self):
        class FakePipeline:
            def foo(self):
                return 'foo'

            def bar(self):
                return 'bar'

        class FakeEntrypoint(Entrypoint):
            def get_pipeline_klass(self) -> Type[Any]:
                return FakePipeline

            def enter(self):
                return self.pipeline.foo(), self.pipeline.bar()

        ep = FakeEntrypoint()
        self.assertEqual(ep.enter(), ('foo', 'bar'))


if __name__ == '__main__':
    TestEntrypoint.run()
