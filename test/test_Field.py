import pytest
from src import Field

@pytest.fixture
def field():
   return Field.Field()

def test_construction(field):
    assert field.turns == 0
    assert field.is_box_checked(0,0) == False
    assert field.is_game_over() == False

def test_turns_increase_after_turn(field):
    field.turn(1,0,0)
    assert field.get_turns() == 1

def test_box_is_checked(field):
    field.turn(1,0,0)
    assert field.is_box_checked(0,0)

def test_who_has_checked_the_box(field):
    field.turn(1,0,0)
    assert field.box_is_checked_by(0,0) == 1

#test pattern
# 1-0-0
# 0-0-0
# 0-0-0
def test_has_player_not_won(field):
    field.turn(1,0,0)
    assert field.has_player_won_horizontal(1)==False
    assert field.has_player_won_vertical(1) == False
    assert field.has_player_won_across(1) == False

#test pattern
# 1-1-1
# 0-0-0
# 0-0-0
def test_has_player_won_horizontal(field):
    field.turn(1,0,0)
    field.turn(1, 0, 1)
    field.turn(1, 0, 2)
    assert field.has_player_won_horizontal(1)
    assert field.is_game_over()
#test pattern
# 1-0-0
# 1-0-0
# 1-0-0
def test_has_player_won_vertical(field):
    field.turn(1,0,0)
    field.turn(1, 1, 0)
    field.turn(1, 2, 0)
    assert field.has_player_won_vertical(1)
    assert field.is_game_over()
#test pattern
# 1-0-0
# 0-1-0
# 0-0-1
def test_has_player_won_across(field):
    field.turn(1,0,0)
    field.turn(1, 1, 1)
    field.turn(1, 2, 2)
    assert field.has_player_won_across(1)
    assert field.is_game_over()
#test pattern turns == 9
# 1-2-1
# 2-1-2
# 2-1-2
def test_is_game_over(field):
    field.turn(1, 0, 0)
    field.turn(2, 0, 1)
    field.turn(1, 0, 2)

    field.turn(2, 1, 0)
    field.turn(1, 1, 1)
    field.turn(2, 1, 2)

    field.turn(2, 2, 0)
    field.turn(1, 2, 1)
    field.turn(2, 2, 2)
    assert field.is_game_over()