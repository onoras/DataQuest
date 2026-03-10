from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Incorrect Contact ID")
        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.contact_type == "physical" and not self.is_verified:
            raise ValueError("Physical contact requires Verifcation")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong Signals should include Message")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        alien_contact1 = AlienContact(
            contact_id="AC_2024_001",
            location="rea 51, Nevada",
            timestamp="2024-05-01T12:30:00",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print(f"ID: {alien_contact1.contact_id}")
        print(f"Type: {alien_contact1.contact_type}")
        print(f"Location: {alien_contact1.location}")
        print(f"Signal: {alien_contact1.signal_strength}")
        print(f"Duration: {alien_contact1.duration_minutes}")
        print(f"Witnesses: {alien_contact1.witness_count}")
        print(f"Message: {alien_contact1.message_received}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e)
    print("======================================")
    try:
        alien_contact1 = AlienContact(
            contact_id="AC_2024_001",
            location="rea 51, Nevada",
            timestamp="2024-05-01T12:30:00",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print(f"ID: {alien_contact1.contact_id}")
        print(f"Type: {alien_contact1.contact_type}")
        print(f"Location: {alien_contact1.location}")
        print(f"Signal: {alien_contact1.signal_strength}")
        print(f"Duration: {alien_contact1.duration_minutes}")
        print(f"Witnesses: {alien_contact1.witness_count}")
        print(f"Message: {alien_contact1.message_received}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e)
