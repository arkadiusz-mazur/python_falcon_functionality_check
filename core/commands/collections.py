from typing import Dict, List

from core.commands import Command


class GetCollectionsCommand(Command):
    def handle(self) -> Dict[str, List[str]]:
        return {
            "collections":
                [
                    "collection1_", "collection_2"
                ]
        }