from typing import TypedDict, List, Annotated
import operator


class InitialDraftState(TypedDict):
    task: dict
    topic: str
    draft: dict


class DraftState(TypedDict):
    task: dict
    topic: str
    draft: dict
    review: str
    revision_notes: str
