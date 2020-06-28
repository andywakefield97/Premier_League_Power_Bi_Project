dataset <- read.csv("D://england-premier-league-matches-2018-to-2019-stats.csv")

dataset$stadium_name[dataset$stadium_name == "John Smith's Stadium (Huddersfield- West Yorkshire)"] <- "The John Smith's Stadium"
dataset$stadium_name[dataset$stadium_name == "Vicarage Road (Watford)"] <- "Vicarage Road Stadium"

output <- dataset