# Wind speed conversions and the beaufort scale - www.101computing.net/wind-force/

forces = {0: ["Calm", "Sea like a mirror", "Smoke rises vertically"],
          1: ["Light air", "Ripples with appearance of scales are formed, without foam crests",
              "Direction shown by smoke drift but not by wind vanes."],
          2: ["Light breeze",
              "Small wavelets still short but more pronounced; crests have a glassy appearance but do not break",
              "Wind felt on face; leaves rustle; wind vane moved by wind."],
          3: ["Gentle breeze",
              "Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses",
              "Leaves and small twigs in constant motion; light flags extended."],
          4: ["Moderate breeze", "Small waves becoming longer; fairly frequent white horses",
              "Raises dust and loose paper; small branches moved."],
          5: ["Fresh breeze",
              "Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray",
              "Small trees in leaf begin to sway; crested wavelets form on inland waters."],
          6: ["Strong breeze",
              "Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray",
              "Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
          7: ["High wind, moderate gale, near gale",
              "Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of "
              "the wind; spindrift begins to be seen",
              "Whole trees in motion; inconvenience felt when walking against the wind."],
          8: ["Gale, fresh gale",
              "Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in "
              "well-marked streaks along the direction of the wind",
              "Twigs break off trees; generally impedes progress."],
          9: ["Strong/severe gale",
              "High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects "
              "visibility",
              "Slight structural damage (chimney pots and slates removed)."],
          10: ["Storm, whole gale",
               "Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white "
               "streaks along the direction of the wind; on the whole the surface of the sea takes on a white "
               "appearance; rolling of the sea becomes heavy; visibility affected",
               "Seldom experienced inland; trees uprooted; considerable structural damage."],
          11: ["Violent storm",
               "Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind "
               "the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests "
               "are blown into foam; visibility affected",
               "Very rarely experienced; accompanied by widespread damage."],
          12: ["Hurricane force",
               "The air is filled with foam and spray; sea is completely white with driving spray; visibility very "
               "seriously affected",
               "Devastation"]
          }

speed = int(input("Enter the speed of the wind in km/h: "))


# Step 1: Convert this speed in knots knowing that 1 knot = 1.852 km/h
def speed_in_knots(speed):
    knot_per_kms = 0.539957
    knots = speed * knot_per_kms
    return knots


# Step 2: Use the Beaufort scale to work out the matching wind force
def beaufort_scale(knots):
    if knots < 1:
        return forces.get(0)
    if 1 < knots < 3:
        return forces.get(1)
    if 4 < knots < 6:
        return forces.get(2)
    if 7 < knots < 10:
        return forces.get(3)
    if 11 < knots < 16:
        return forces.get(4)
    if 17 < knots < 21:
        return forces.get(5)
    if 22 < knots < 27:
        return forces.get(6)
    if 28 < knots < 33:
        return forces.get(7)
    if 34 < knots < 40:
        return forces.get(8)
    if 41 < knots < 47:
        return forces.get(9)
    if 48 < knots < 55:
        return forces.get(10)
    if 56 < knots < 63:
        return forces.get(11)
    if knots > 64:
        return forces.get(12)


# Step 3: Display the wind force, description, sea conditions and land conditions corresponding to this wind force


# Step 4: Review the code in step 1 to allow the user to enter the wind speed in the unit of their choice (km/h, mph,
# knots)


knots = speed_in_knots(speed)
print(f"Speed in Knots: {speed_in_knots(speed)}")
print(beaufort_scale(knots))
