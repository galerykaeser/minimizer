(define (problem lights-1A-0-1-0-0B)
(:domain lights)
;
; Room1 Room2 Room3 Room4 Room5
; 1A    0     1     0     0B
;
(:objects
    room1
    room2
    room3
    room4
    room5
)
(:init
    (light-on room1)
    (light-on room3)
    (a-is-in room1)
    (b-is-in room5)

    (first-room room1)
    (next-room room1 room2)
    (next-room room2 room3)
    (next-room room3 room4)
    (next-room room4 room5)
    (last-room room5)
)
(:goal (and
    (a-is-in room3)
    (b-is-in room3)
))
)
