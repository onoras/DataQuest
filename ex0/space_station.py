from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)


def main():
    print("========================================")
    print("Valid station created:")
    try:
        spacestation1 = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-05-01T12:30:00"
        )
        print(f"ID: {spacestation1.station_id}")
        print(f"Name: {spacestation1.name}")
        print(f"Crew: {spacestation1.crew_size}")
        print(f"Power: {spacestation1.power_level}")
        print(f"Oxygen: {spacestation1.oxygen_level}")
        if spacestation1.is_operational:
            print("Status: Operational")
        else:
            print("Status not Operational")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e)
    print("========================================")
    try:
        spacestation2 = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-05-01T12:30:00"
        )
        print(f"ID: {spacestation2.station_id}")
        print(f"Name: {spacestation2.name}")
        print(f"Crew: {spacestation2.crew_size}")
        print(f"Power: {spacestation2.power_level}")
        print(f"Oxygen: {spacestation2.oxygen_level}")
        if spacestation2.is_operational:
            print("Status: Operational")
        else:
            print("Status not Operational")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

if __name__ == "__main__":
    print("Space Station Data Validation")
    main()
