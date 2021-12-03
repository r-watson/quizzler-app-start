#  data type hints. specify desired data type so line will be highlighted in IDE and you'll get tooltip with info.
#  place desired data type after colon (:)

age: int
name: str
height: float
is_human: bool

age = 12
name = 12
height = 12

#  type arrows specify the desired type for a function/method output. place after arrow ->.
def police_check(age_check: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return True

if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")