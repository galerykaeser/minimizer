(define
 (domain robot)
 (:requirements :strips :disjunctive-preconditions)
 (:types PACKAGE ROOM ROOMDOOR HTN_ID)
 (:predicates
  (armempty)
  (rloc ?loc - ROOM)
  (in ?obj - PACKAGE ?loc - ROOM)
  (holding ?obj - PACKAGE)
  (closed ?d - ROOMDOOR)
  (door ?loc1 ?loc2 - ROOM ?d - ROOMDOOR)
  (goal_in ?obj - PACKAGE ?loc - ROOM)
  (htn_top_id ?htn_id1 - HTN_ID)
  (htn_next_id ?htn_id1 ?htn_id2 - HTN_ID)
  (htn_used_id ?htn_id1 - HTN_ID)
  (htn_first_free ?htn_id1 - HTN_ID)
  (htn_next_free ?htn_id1 ?htn_id2 - HTN_ID)
  (htn_constrains ?htn_id1 ?htn_id2 - HTN_ID)
  (htn_finished)
  (htn_task_achieve-goals ?htn_id1 - HTN_ID)
  (htn_task_pickup ?htn_id1 - HTN_ID)
  (htn_task_putdown ?htn_id1 - HTN_ID))
  
 (:derived
  (htn_used_block ?htn_id1 ?htn_id2 - HTN_ID)
  (htn_next_id ?htn_id1 ?htn_id2))
  
 (:derived
  (htn_used_block ?htn_id1 ?htn_id2 - HTN_ID)
  (exists
   (?htn_id3 - HTN_ID)
   (and
    (htn_next_id ?htn_id3 ?htn_id2)
    (htn_used_id ?htn_id3)
    (htn_used_block ?htn_id1 ?htn_id3))))
  
 (:derived
  (htn_next_free ?htn_id1 ?htn_id2 - HTN_ID)
  (and
   (not (htn_used_id ?htn_id2))
   (htn_used_block ?htn_id1 ?htn_id2)))
  
 (:derived
  (htn_first_free ?htn_id1 - HTN_ID)
  (and (htn_top_id ?htn_id1) (not (htn_used_id ?htn_id1))))
  
 (:derived
  (htn_first_free ?htn_id1 - HTN_ID)
  (exists
   (?htn_id2 - HTN_ID)
   (and
    (htn_top_id ?htn_id2)
    (htn_used_id ?htn_id2)
    (htn_next_free ?htn_id2 ?htn_id1))))
  
 (:derived
  (htn_finished)
  (forall (?htn_id1 - HTN_ID) (not (htn_used_id ?htn_id1))))
  
 (:action achieve-goals
  :parameters (?htn_id1 ?htn_id2 ?htn_id3 - HTN_ID)
  :precondition (and
                 (htn_task_achieve-goals ?htn_id1)
                 (forall
                  (?htn_id0 - HTN_ID)
                  (not (htn_constrains ?htn_id0 ?htn_id1)))
                 (htn_first_free ?htn_id2)
                 (htn_next_free ?htn_id2 ?htn_id3))
  :effect (and
           (not (htn_task_achieve-goals ?htn_id1))
           (htn_task_achieve-goals ?htn_id1)
           (htn_task_pickup ?htn_id2)
           (htn_task_putdown ?htn_id3)
           (htn_used_id ?htn_id2)
           (htn_used_id ?htn_id3)
           (htn_constrains ?htn_id2 ?htn_id3)
           (htn_constrains ?htn_id3 ?htn_id1)))
  
 (:action finished
  :parameters (?htn_id1 - HTN_ID)
  :precondition (and
                 (htn_task_achieve-goals ?htn_id1)
                 (forall
                  (?htn_id2 - HTN_ID)
                  (not (htn_constrains ?htn_id2 ?htn_id1)))
                 (forall
                  (?obj - PACKAGE ?loc - ROOM)
                  (and (goal_in ?obj ?loc) (in ?obj ?loc))))
  :effect (and
           (not (htn_task_achieve-goals ?htn_id1))
           (not (htn_used_id ?htn_id1))
           (forall
            (?htn_id2 - HTN_ID)
            (not (htn_constrains ?htn_id1 ?htn_id2)))))
  
 (:action open
  :parameters (?loc1 ?loc2 - ROOM ?d - ROOMDOOR)
  :precondition (and (rloc ?loc1) (door ?loc1 ?loc2 ?d) (closed ?d))
  :effect (not (closed ?d)))
  
 (:action move
  :parameters (?loc1 ?loc2 - ROOM ?d - ROOMDOOR)
  :precondition (and
                 (rloc ?loc1)
                 (door ?loc1 ?loc2 ?d)
                 (not (closed ?d)))
  :effect (and (rloc ?loc2) (not (rloc ?loc1))))
  
 (:action putdown
  :parameters (?obj - PACKAGE ?loc - ROOM ?htn_id1 - HTN_ID)
  :precondition (and
                 (htn_task_putdown ?htn_id1)
                 (forall
                  (?htn_id2 - HTN_ID)
                  (not (htn_constrains ?htn_id2 ?htn_id1)))
                 (rloc ?loc)
                 (holding ?obj)
                 (goal_in ?obj ?loc))
  :effect (and
           (not (htn_task_putdown ?htn_id1))
           (not (htn_used_id ?htn_id1))
           (forall
            (?htn_id2 - HTN_ID)
            (not (htn_constrains ?htn_id1 ?htn_id2)))
           (not (holding ?obj))
           (armempty)
           (in ?obj ?loc)))
  
 (:action pickup
  :parameters (?obj - PACKAGE ?loc - ROOM ?htn_id1 - HTN_ID)
  :precondition (and
                 (htn_task_pickup ?htn_id1)
                 (forall
                  (?htn_id2 - HTN_ID)
                  (not (htn_constrains ?htn_id2 ?htn_id1)))
                 (armempty)
                 (rloc ?loc)
                 (in ?obj ?loc)
                 (not (goal_in ?obj ?loc)))
  :effect (and
           (not (htn_task_pickup ?htn_id1))
           (not (htn_used_id ?htn_id1))
           (forall
            (?htn_id2 - HTN_ID)
            (not (htn_constrains ?htn_id1 ?htn_id2)))
           (not (in ?obj ?loc))
           (not (armempty))
           (holding ?obj))))
