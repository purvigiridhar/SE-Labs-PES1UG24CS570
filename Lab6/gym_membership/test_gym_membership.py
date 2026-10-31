
import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ---------------- MEMBERSHIP COST TESTS ----------------

def test_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_quarterly_plan():
    assert membership_cost("quarterly", 30, False, False) == 4000


def test_yearly_plan():
    assert membership_cost("yearly", 30, False, False) == 12000


def test_invalid_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_age_below_14():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_student_discount():
    assert membership_cost("monthly", 20, True, False) == 1350


def test_trainer_addon():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_yearly_trainer_discount():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_senior_with_trainer():
    assert membership_cost("monthly", 60, False, True) == 3125


# ---------------- CAN ENTER TESTS ----------------

def test_can_enter():
    assert can_enter(10, True, False, "M") is True


def test_inactive_plan():
    assert can_enter(10, False, False, "M") is False


def test_before_opening_time():
    assert can_enter(4, True, False, "M") is False


def test_after_closing_time():
    assert can_enter(23, True, False, "M") is False


def test_opening_boundary():
    assert can_enter(5, True, False, "M") is True


def test_closing_boundary():
    assert can_enter(22, True, False, "M") is True


def test_women_only_slot_female():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male():
    assert can_enter(10, True, True, "M") is False


# ---------------- BMI CATEGORY TESTS ----------------

def test_invalid_height():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(60, 0)


def test_underweight():
    assert bmi_category(45, 1.7) == "underweight"


def test_normal_weight():
    assert bmi_category(60, 1.7) == "normal"


def test_overweight():
    assert bmi_category(75, 1.7) == "overweight"


def test_obese():
    assert bmi_category(90, 1.7) == "obese"
