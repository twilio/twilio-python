from twilio.base.values import of, unset


def test_of_removes_unset_values():
    result = of(
        {
            "foo": "bar",
            "unset": unset,
        }
    )

    assert result == {
        "foo": "bar",
    }


class EqualToUnset:
    def __eq__(self, other):
        return other is unset


def test_of_only_removes_unset_sentinel():
    value = EqualToUnset()

    result = of(
        {
            "value": value,
            "unset": unset,
        }
    )

    assert result == {
        "value": value,
    }
