height <- c(150, 160, 165, 170, 175, 180)  # in centimeters
weight <- c(50, 60, 65, 70, 75, 80)         # in kilograms

women_data <- data.frame(
  Height = height,
  Weight = weight
)

# Create a factor for height categories
height_factor <- cut(women_data$Height, 
                     breaks = c(140, 160, 170, 180, 190), 
                     labels = c("140-160 cm", "160-170 cm", "170-180 cm", "180-190 cm"),
                     right = FALSE)

# Add the factor to the data frame
women_data$HeightCategory <- height_factor

print(women_data)
