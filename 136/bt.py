"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}


# complete :
def check_bt(donor, recipient):
    if isinstance(donor, int) and isinstance(recipient, int):
        if donor < 0 or donor > 7 or recipient < 0 or recipient > 7:
            raise ValueError
    elif isinstance(donor, str) and isinstance(recipient, str):
        if donor not in blood_type_text or recipient not in blood_type_text:
            raise ValueError
        donor, recipient = blood_type_text[donor], blood_type_text[recipient]
    elif not isinstance(donor, Bloodtype) or not isinstance(recipient, Bloodtype):
        raise TypeError
    if recipient == Bloodtype.AB_POS:
        return donor in (
            Bloodtype.ZERO_NEG,
            Bloodtype.ZERO_POS,
            Bloodtype.A_NEG,
            Bloodtype.A_POS,
            Bloodtype.B_NEG,
            Bloodtype.B_POS,
            Bloodtype.AB_NEG,
            Bloodtype.AB_POS,
        )
    if donor == Bloodtype.ZERO_NEG:
        # return recipient in (Bloodtype.ZERO_NEG, Bloodtype.ZERO_POS)
        return recipient in (
            Bloodtype.ZERO_NEG,
            Bloodtype.ZERO_POS,
            Bloodtype.A_NEG,
            Bloodtype.A_POS,
            Bloodtype.B_NEG,
            Bloodtype.B_POS,
            Bloodtype.AB_NEG,
            Bloodtype.AB_POS,
        )
    elif donor == Bloodtype.ZERO_POS:
        return recipient in (
            Bloodtype.ZERO_POS,
            Bloodtype.A_POS,
            Bloodtype.B_POS,
            Bloodtype.AB_POS,
        )
    elif donor == Bloodtype.B_NEG:
        return recipient in (
            Bloodtype.B_NEG,
            Bloodtype.B_POS,
            Bloodtype.AB_NEG,
            Bloodtype.AB_POS,
        )
    elif donor == Bloodtype.B_POS:
        return recipient in (Bloodtype.B_POS, Bloodtype.AB_POS)
    elif donor == Bloodtype.A_NEG:
        return recipient in (
            Bloodtype.A_NEG,
            Bloodtype.A_POS,
            Bloodtype.AB_NEG,
            Bloodtype.AB_POS,
        )
    elif donor == Bloodtype.A_POS:
        return recipient in (Bloodtype.A_POS, Bloodtype.AB_POS)
    elif donor == Bloodtype.AB_NEG:
        return recipient == Bloodtype.AB_NEG
    elif donor == Bloodtype.AB_POS:
        return True
    return False


# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )
