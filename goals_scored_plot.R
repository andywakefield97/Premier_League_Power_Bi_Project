
library(ggplot2)

plot <- qplot(x = reorder(Team, general_league_position), 
              attack_scored, 
              data=dataset, 
              color = general_league_position,
              geom = c("point", "line"),
              main = "",
              xlab = "Premier League Team",
              ylab = "Sum of goals scored")

plot + theme(axis.text.x = element_text(angle = 45))