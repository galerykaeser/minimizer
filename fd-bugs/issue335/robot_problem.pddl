(define
 (problem test_3_1)
 (:domain robot)
 (:objects o1 - PACKAGE
           c r1 r2 r3 - ROOM
           d03 d01 d12 - ROOMDOOR
           htn_id1 htn_id2 htn_id3 - HTN_ID)
 (:init
  (rloc c)
  (armempty)
  (door c r1 d01)
  (door c r3 d03)
  (door r1 c d01)
  (door r1 r2 d12)
  (door r2 r1 d12)
  (door r3 c d03)
  (closed d03)
  (closed d01)
  (in o1 r2)
  (goal_in o1 r1)
  (htn_task_achieve-goals htn_id1)
  (htn_used_id htn_id1)
  (htn_top_id htn_id1)
  (htn_next_id htn_id1 htn_id2)
  (htn_next_id htn_id2 htn_id3))
 (:goal (and (htn_finished) (in o1 r1))))