dataset <- read.csv("D://england-premier-league-matches-2018-to-2019-stats.csv")

dataset$stadium_name[dataset$stadium_name == "John Smith's Stadium (Huddersfield- West Yorkshire)"] <- "The John Smith's Stadium"
dataset$stadium_name[dataset$stadium_name == "Vicarage Road (Watford)"] <- "Vicarage Road Stadium"
dataset$goal_diff <- with(dataset, (home_team_goal_count - away_team_goal_count))

library(pacman)
pacman :: p_load(stringr)
pacman :: p_load(dplyr)

output<- dataset %>%
  filter(str_detect(home_team_goal_timings, "90")| str_detect(away_team_goal_timings, "90"),
         dataset$goal_diff == 0 | dataset$goal_diff == -1 | dataset$goal_diff == 1)