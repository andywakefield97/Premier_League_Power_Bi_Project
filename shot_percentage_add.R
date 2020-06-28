prem_data <- dataset
prem_data$home_shot_percentage <- with(prem_data, (prem_data$home_team_shots_on_target / prem_data$home_team_shots)*100)

prem_data$away_shot_percentage <- with(prem_data, (prem_data$away_team_shots_on_target / prem_data$away_team_shots)*100)


dataset <- subset(prem_data, select = c(home_team_name, away_team_name, home_shot_percentage, away_shot_percentage))