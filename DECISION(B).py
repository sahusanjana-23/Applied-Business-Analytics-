# Expected Value Calculation

# Launch Product
prob_high = 0.60
profit_high = 100000

prob_low = 0.40
loss_low = -30000

# Do Not Launch
profit_no_launch = 20000

# Calculate Expected Values
EV_launch = (
    prob_high * profit_high +
    prob_low * loss_low
)

EV_no_launch = profit_no_launch

# Display
print("Expected Value of Launching:", EV_launch)
print("Expected Value of Not Launching:", EV_no_launch)

# Select alternative
if EV_launch > EV_no_launch:
    print("Selected Alternative: Launch Product")
else:
    print("Selected Alternative: Do Not Launch")
s
