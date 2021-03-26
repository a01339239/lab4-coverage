from dataclasses import dataclass, asdict
from uuid import uuid4
from typing import Optional, List
from pathlib import Path
from json import dump as jdump, load as jload
from pprint import pprint


@dataclass
class Record:
    name: str
    email: str
    age: int
    country_of_origin: str
    id: Optional[str] = None

    def __post_init__(self):
        self.id = self.id or str(uuid4())


class Directory:
    file_path = Path.joinpath(Path.cwd(), "lab3", "directory.json")

    def __init__(self):
        self.file_path.write_text("[]")

    def add_record(self, record: Record):
        with open(self.file_path, "r+") as file:
            directory = jload(file)
            directory.append(asdict(record))
            file.seek(0)
            file.truncate()
            jdump(directory, file)

    def delete_record(self, id: str) -> int:
        records_deleted = 0
        with open(self.file_path, "r+") as file:
            directory = jload(file)
            index = 0
            while index < len(directory):
                record = directory[index]
                if record["id"] == id:
                    del directory[index]
                    records_deleted += 1
                    index -= 1
                index += 1
            file.seek(0)
            file.truncate()
            jdump(directory, file)
        return records_deleted

    def look_for_record(
        self, email: Optional[str] = None, age: Optional[int] = None
    ) -> List[Record]:
        match_records = list()
        if any((email, age)):
            with open(self.file_path, "r") as file:
                directory = jload(file)
                for record in directory:
                    if record["email"] == email or record["age"] == age:
                        match_records.append(Record(**record))
        return match_records

    def display_all_records(self):
        with open(self.file_path, "r") as file:
            directory = jload(file)
            pprint(directory)
