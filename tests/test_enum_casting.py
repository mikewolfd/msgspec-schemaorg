#!/usr/bin/env python3
"""
Test enum usage behavior in Schema.org models.
"""

import msgspec

from msgspec_schemaorg.models.event import DeliveryEvent
from msgspec_schemaorg.enums.intangible.DeliveryMethod import DeliveryMethod


def test_enum_usage():
    """Test basic enum behavior with msgspec models."""
    # 1. Test passing an enum value directly
    event1 = DeliveryEvent(hasDeliveryMethod=DeliveryMethod.LockerDelivery)
    assert isinstance(event1.hasDeliveryMethod, DeliveryMethod)
    assert event1.hasDeliveryMethod == DeliveryMethod.LockerDelivery
    assert event1.hasDeliveryMethod.value == "LockerDelivery"
    
    # 2. Test passing a string value (not automatically converted to enum)
    event2 = DeliveryEvent(hasDeliveryMethod="LockerDelivery")
    assert isinstance(event2.hasDeliveryMethod, str)
    assert event2.hasDeliveryMethod == "LockerDelivery"
    
    # 3. Test string values still compare equal to enum values
    assert event2.hasDeliveryMethod == DeliveryMethod.LockerDelivery.value
    
    # 4. Test passing a list of enum values
    event3 = DeliveryEvent(hasDeliveryMethod=[
        DeliveryMethod.LockerDelivery, 
        DeliveryMethod.ParcelService
    ])
    assert isinstance(event3.hasDeliveryMethod, list)
    assert all(isinstance(item, DeliveryMethod) for item in event3.hasDeliveryMethod)
    
    # 5. Test passing a list of strings
    event4 = DeliveryEvent(hasDeliveryMethod=["LockerDelivery", "ParcelService"])
    assert isinstance(event4.hasDeliveryMethod, list)
    assert all(isinstance(item, str) for item in event4.hasDeliveryMethod)
    
    # 6. Test encoding to JSON (both should serialize identically)
    json_bytes1 = msgspec.json.encode(event1)
    json_bytes2 = msgspec.json.encode(event2)
    assert json_bytes1 == json_bytes2
    
    # In both cases, enums are serialized as their string value
    json_str = json_bytes1.decode()
    assert '"hasDeliveryMethod":"LockerDelivery"' in json_str
    
    # 7. Test invalid values are allowed (no validation against enum)
    event5 = DeliveryEvent(hasDeliveryMethod="InvalidDeliveryMethod")
    assert event5.hasDeliveryMethod == "InvalidDeliveryMethod"
    
    print("All enum usage tests passed!")


if __name__ == "__main__":
    test_enum_usage() 