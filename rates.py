def Rate(Rate, WhichRate, RateEmbed):
  if Rate > 70:
    Howratey = "That is extremely " + WhichRate
  elif Rate > 40:
    Howratey = "That is quite " + WhichRate
  elif Rate > 20:
    Howratey = "That is slightly " + WhichRate
  else:
    Howratey = "That is a not that " + WhichRate
  RateEmbed.set_footer(text = Howratey)
