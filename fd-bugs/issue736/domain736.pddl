(define (domain lights)
; A (hates the dark)
; - if light in A's room is switched out:
;     - if one neighboring room is bright: move there (prefer the right one)
;     - if both neighboring room are dark: move to one neighbor (prefer the left one)
;
; B (avoids the light)
; - if light in B's room is switched on:
;     - if one neighboring room is dark: move there (prefer the left one)
;     - if both neighboring room are bright: move to one neighbor (prefer the right one)
;
    (:requirements :conditional-effects)
    (:predicates
        (light-on ?r)
        (a-is-in ?r)
        (b-is-in ?r)
        ;
        ; static predicates
        (next-room ?r ?rn)
        (first-room ?r)
        (last-room ?r)
    )

    (:action toggle-light-center-room
        :parameters (?leftroom ?room ?rightroom)
        :precondition (and
            (next-room ?leftroom ?room)
            (next-room ?room ?rightroom)
        )
        :effect (and
            (when (light-on ?room) (and
                (not (light-on ?room))
                (when (a-is-in ?room) (and
                    (when (light-on ?rightroom) (and
                        (not (a-is-in ?room))
                        (a-is-in ?rightroom)
                    ))
                    (when (and (not (light-on ?rightroom)) (light-on ?leftroom)) (and
                        (not (a-is-in ?room))
                        (a-is-in ?leftroom)
                    ))
                    (when (and (not (light-on ?rightroom)) (not (light-on ?leftroom))) (and
                        (not (a-is-in ?room))
                        (a-is-in ?leftroom)
                    ))
                ))
            ))
            (when (not (light-on ?room)) (and
                (light-on ?room)
                (when (b-is-in ?room) (and
                    (when (not (light-on ?leftroom)) (and
                        (not (b-is-in ?room))
                        (b-is-in ?leftroom)
                    ))
                    (when (and (light-on ?leftroom) (not (light-on ?rightroom))) (and
                        (not (b-is-in ?room))
                        (b-is-in ?rightroom)
                    ))
                    (when (and (light-on ?leftroom) (light-on ?rightroom)) (and
                        (not (b-is-in ?room))
                        (b-is-in ?rightroom)
                    ))
                ))
            ))
        )
    )

    (:action toggle-light-first-room
        :parameters (?room ?rightroom)
        :precondition (and
            (first-room ?room)
            (next-room ?room ?rightroom)
        )
        :effect (and
            (when (light-on ?room) (and
                (not (light-on ?room))
                (when (a-is-in ?room) (and
                    (not (a-is-in ?room))
                    (a-is-in ?rightroom)
                ))
            ))
            (when (not (light-on ?room)) (and
                (light-on ?room)
                (when (b-is-in ?room) (and
                    (not (b-is-in ?room))
                    (b-is-in ?rightroom)
                ))
            ))
        )
    )

    (:action toggle-light-last-room
        :parameters (?leftroom ?room)
        :precondition (and
            (last-room ?room)
            (next-room ?leftroom ?room)
        )
        :effect (and
            (when (light-on ?room) (and
                (not (light-on ?room))
                (when (a-is-in ?room) (and
                    (not (a-is-in ?room))
                    (a-is-in ?leftroom)
                ))
            ))
            (when (not (light-on ?room)) (and
                (light-on ?room)
                (when (b-is-in ?room) (and
                    (not (b-is-in ?room))
                    (b-is-in ?leftroom)
                ))
            ))
        )
    )
)
