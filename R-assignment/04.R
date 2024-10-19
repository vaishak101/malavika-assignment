data_frame <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David"),
  Age = c(25, 30, 35, 40),
  Score = c(85.5, 90.0, 78.5, 88.0),
  Passed = c(TRUE, TRUE, FALSE, TRUE)
)

summary_stats <- summary(data_frame)

data_structure <- str(data_frame)

cat("Statistical Summary:\n")
print(summary_stats)
cat("\nNature of the Data (Structure):\n")
print(data_structure)
