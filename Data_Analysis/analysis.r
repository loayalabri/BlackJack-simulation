library(dplyr)
data <- read.csv("Data/first_run_200.csv", header = TRUE)

data_summary <- data %>% group_by(
    replicate,
    num_decks, 
    strategy,
    dealer_behaviour
) %>% summarise(
    total_bet = sum(bet),
    cumilative_outcome = last(cumilative_outcome),
    num_hands = n(), # = 100 always
    .groups = "drop"
)

data_summary$ROI <- (data_summary$cumilative_outcome / data_summary$total_bet) * 100
write.csv(data_summary, "Data/firs_run_summary.csv", row.names=FALSE)

print(head(data_summary))




