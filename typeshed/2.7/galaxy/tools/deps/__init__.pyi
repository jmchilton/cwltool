# Stubs for galaxy.tools.deps (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .resolvers import NullDependency as NullDependency
from .resolvers.conda import CondaDependencyResolver as CondaDependencyResolver
from .resolvers.galaxy_packages import GalaxyPackageDependencyResolver as GalaxyPackageDependencyResolver
from .resolvers.tool_shed_packages import ToolShedPackageDependencyResolver as ToolShedPackageDependencyResolver

log = ...  # type: Any
EXTRA_CONFIG_KWDS = ...  # type: Any
CONFIG_VAL_NOT_FOUND = ...  # type: Any

def build_dependency_manager(config: Any): ...  # type: DependencyManager

class NullDependencyManager:
    dependency_resolvers = ...  # type: Any
    def uses_tool_shed_dependencies(self): ...
    def dependency_shell_commands(self, requirements, **kwds): ...
    def find_dep(self, name, version: Optional[Any] = ..., type: str = ..., **kwds): ...

class DependencyManager:
    extra_config = ...  # type: Any
    default_base_path = ...  # type: Any
    resolver_classes = ...  # type: Any
    dependency_resolvers = ...  # type: Any
    def __init__(self, default_base_path, conf_file: Optional[Any] = ..., **extra_config) -> None: ...
    def dependency_shell_commands(self, requirements, **kwds): ...
    def requirements_to_dependencies(self, requirements, **kwds): ...
    def uses_tool_shed_dependencies(self): ...
    def find_dep(self, name, version: Optional[Any] = ..., type: str = ..., **kwds): ...
