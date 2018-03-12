from favourite_number import remember_number
from get_number import output_number

try:
    output_number()
except FileNotFoundError:
    remember_number()