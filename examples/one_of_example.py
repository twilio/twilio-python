"""
Example demonstrating oneOf functionality in the Twilio Python SDK.

This example shows how to use the Pet API which implements oneOf schema patterns.
The Cat schema uses allOf + oneOf, allowing two different variants:
1. Variant "One": Cat with param1, param2, and a nested dog object
2. Variant "Two": Cat with object1 and object2

Based on the OpenAPI spec at /v1/pets endpoint.
"""

import os
from twilio.rest import Client
from twilio.rest.one_of.v1 import V1
from twilio.rest.one_of.v1.pet import PetList
from twilio.base.domain import Domain

# Initialize Twilio client credentials
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def example_create_pet_variant_one():
    """
    Example: Create a pet using Cat variant "One"

    This variant includes:
    - account_sid (from base Cat schema)
    - param1, param2 (from "One" schema)
    - dog (nested Dog object from "One" schema)
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Create a Dog object for the nested property
    dog = PetList.Dog({
        "type": "dog",
        "name": "Buddy",
        "pack_size": 5
    })

    # Create Cat with variant "One" (param1, param2, dog)
    cat = PetList.Cat({
        "account_sid": ACCOUNT_SID,
        "param1": "first_parameter",
        "param2": "second_parameter",
        "dog": dog
    })

    try:
        # Initialize the OneOf domain and create the pet
        one_of_domain = Domain(client, "https://oneOf.twilio.com")
        v1 = V1(one_of_domain)
        pet = v1.pets.create(cat=cat)

        print("Successfully created pet with variant 'One':")
        print(f"  Account SID: {pet.account_sid}")
        print(f"  Param1: {pet.param1}")
        print(f"  Param2: {pet.param2}")
        print(f"  Dog: {pet.dog}")
        return pet

    except Exception as e:
        print(f"Error creating pet: {e}")
        return None


def example_create_pet_variant_two():
    """
    Example: Create a pet using Cat variant "Two"

    This variant includes:
    - account_sid (from base Cat schema)
    - object1, object2 (from "Two" schema)
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Create Cat with variant "Two" (object1, object2)
    cat = PetList.Cat({
        "account_sid": ACCOUNT_SID,
        "object1": "first_object",
        "object2": "second_object"
    })

    try:
        # Initialize the OneOf domain and create the pet
        one_of_domain = Domain(client, "https://oneOf.twilio.com")
        v1 = V1(one_of_domain)
        pet = v1.pets.create(cat=cat)

        print("Successfully created pet with variant 'Two':")
        print(f"  Account SID: {pet.account_sid}")
        print(f"  Object1: {pet.object1}")
        print(f"  Object2: {pet.object2}")
        return pet

    except Exception as e:
        print(f"Error creating pet: {e}")
        return None


def example_create_pet_inline():
    """
    Example: Create a pet with inline Dog object construction

    This shows a more concise way to create the Cat object with
    nested objects defined inline.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Create Cat with inline Dog object
    cat = PetList.Cat({
        "account_sid": ACCOUNT_SID,
        "param1": "inline_param1",
        "param2": "inline_param2",
        "dog": PetList.Dog({
            "type": "dog",
            "name": "Max",
            "pack_size": 3
        })
    })

    try:
        one_of_domain = Domain(client, "https://oneOf.twilio.com")
        v1 = V1(one_of_domain)
        pet = v1.pets.create(cat=cat)

        print("Successfully created pet with inline approach:")
        print(f"  Account SID: {pet.account_sid}")
        print(f"  Param1: {pet.param1}")
        return pet

    except Exception as e:
        print(f"Error creating pet: {e}")
        return None


async def example_create_pet_async():
    """
    Example: Create a pet asynchronously

    The SDK supports async operations using the create_async method.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    cat = PetList.Cat({
        "account_sid": ACCOUNT_SID,
        "param1": "async_param1",
        "param2": "async_param2",
        "dog": PetList.Dog({
            "type": "dog",
            "name": "Charlie",
            "pack_size": 2
        })
    })

    try:
        one_of_domain = Domain(client, "https://oneOf.twilio.com")
        v1 = V1(one_of_domain)
        pet = await v1.pets.create_async(cat=cat)

        print("Asynchronously created pet:")
        print(f"  Account SID: {pet.account_sid}")
        print(f"  Param1: {pet.param1}")
        return pet

    except Exception as e:
        print(f"Error creating pet async: {e}")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("OneOf Pattern Examples - Pet API")
    print("=" * 60)

    print("\n1. Creating pet with variant 'One' (param1, param2, dog):")
    print("-" * 60)
    example_create_pet_variant_one()

    print("\n2. Creating pet with variant 'Two' (object1, object2):")
    print("-" * 60)
    example_create_pet_variant_two()

    print("\n3. Creating pet with inline Dog construction:")
    print("-" * 60)
    example_create_pet_inline()

    print("\n4. Creating pet asynchronously:")
    print("-" * 60)
    import asyncio
    asyncio.run(example_create_pet_async())

    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
