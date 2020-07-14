# pygames
River Game:

1 player chooses to collect objects appearing on the screen. 

objects:
each object has 3 attributes (shape, fill-pattern, cluster-count)
	each attribute has 1 of 3 values:
		shape - round, square, triangle
		fill-pattern - solid, empty, dotted
		cluster-count - one, two, three


HUD:
Current Score
High Score (for game instance)
Game Clock (how many HH:MM:SS have passed since score was = 0)
High Score Clock (longest game clock achieved for game instance) 
Game score and clock begin at zero
Several objects appear on screen (in the river)
Player appears on screen in the river

rules: 
If player clicks an object, they collect it, trigger the start of the game clock, and are awarded points:
	in any 10 second epoch:
		+1 point each for collecting object 1 & 2
		+2 points for collecting 3rd object
		+4 points for collecting 4th object
		+8 points for collecting 5th object
		+16 points for collecting 6th object
		+32 points for collecting 7th object
		+64 points for collecting 8th object
		+128 points for collecting 9th object
		+256 each point for collecting 10 or more objects

If 10 seconds pass and player does not collect subsequent object, 1 point is subtracted from score

If score drops to zero, game clock is reset to zero

When an object is collected, it becomes the "last collected object"

If an object is collected and shares any attributes with the "last collected object", score drops to zero and clock is set to zero (essentially game end)

goals:
player can play for score - encouraged to take risks by making decisions as fast as possible
player can play for clock - lazy river style, clock keeps going as long as score is >0
