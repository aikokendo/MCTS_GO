#!/usr/bin/python
import node
import datetime
import board
import copy
import random
import multiprocessing
import threading


class MonteCarlo:
    def __init__(self, state, roles):
        self.roles = roles
        self.state = state
        self.results = []
        self.scores = []

    def best_next_move_for_thread(self):
        start_time = datetime.datetime.now()
        # create root
        root_state = copy.deepcopy(self.state)
        v0 = node.Node(root_state, 0, 0, None, [])
        while (datetime.datetime.now() - start_time).seconds < 1:
            v1 = self.select(v0)
            score = self.simulate(v1.state, 1)
            v1.back_propagate(score)
        best_child = v0.best_child()
        score = v0.best_child_score
        self.results.append((best_child.state.last_x, best_child.state.last_y))
        self.scores.append((best_child.state.last_x, best_child.state.last_y, score))

    def select(self, v):
        if v.state.has_actions():
            return self.expand(v)
        else:
            return v.best_child()
            # select node for expansion based on the visit count.

    def expand(self, v):
        random_action = random.sample(v.state.actions, 1)
        simulated_board = copy.deepcopy(v.state)
        threat_result = v.state.check_threat(True)
        if threat_result != None:
            print("I CAN ATTACK")
            simulated_board.add_piece(threat_result[0],threat_result[1],self.roles.get_current_ai())
        else:
            simulated_board.add_piece(random_action[0][0], random_action[0][1], self.roles.get_current_ai())
        v_child = node.Node(simulated_board, 0, 0, v, [])
        v.children.append(v_child)
        if threat_result != None:
            v.state.remove_action(threat_result[0],threat_result[1])
        else:
            v.state.remove_action(random_action[0][0], random_action[0][1])
        return v_child
        # expand a selected node by all the possible actions it has available.

    def simulate(self, state, level):
        # simulate player movements up to getting a winner. Assign a value to the result (depthcharge)
        # use simulate to best guess how much valuable a branch is.
        # assume expansion will call it after an action of current user
        if level == 1:
            result = state.is_terminal(self.roles.get_current_ai())
            if result == 1:  # tie
                return 0
            if result == 2:
                return 100  # full reward since we are in level 1
        simulated_board = copy.deepcopy(state)
        players_list = self.roles.player_array_for_montecarlo()
        for i in players_list:
            actions = simulated_board.actions
            random_action = random.sample(actions, 1)
            simulated_board.add_piece(random_action[0][0], random_action[0][1], i)
            result = simulated_board.is_terminal(i)
            if result == 1:  # tie
                return 0
            if result == 2:
                if i == self.roles.get_current_ai():  # current player won
                    if level < 35:
                        return 30
                    return 100 - level*2  # reduced reward based on level
                else:
                    return -100  # current player lost
        return self.simulate(simulated_board, level + 1)

    def best_next_move(self):
        processors = multiprocessing.cpu_count()
        threads = []
        for i in range(processors):
            t = threading.Thread(target=self.best_next_move_for_thread)
            threads.append(t)
        for j in threads:
            j.start()

        for j in threads:
            j.join()

        # threads done! lets select our best next move:
        print(self.scores)
        max = 0
        finalResult = set()
        for item in self.results:
            current = self.results.count(item)
            if current > max:
                max = current
                finalResult.clear()
                finalResult.add(item)
            if current == max:
                finalResult.add(item)

        if (len(finalResult)) > 1:
            max_score = 0
            move = ()
            for item in finalResult:
                for i in self.scores:
                    if i[0] == item[0] and i[1] == item[1] and i[2] >= max_score:
                        max_score = i[2]
                        move = item
            finalResult.clear()
            finalResult.add(move)

        best_move = finalResult.pop()
        temp_state = copy.deepcopy(self.state)
        temp_state.add_piece(best_move[0],best_move[1], self.roles.get_current_ai())
        if temp_state.is_terminal(self.roles.get_current_ai()) != 2:
            result = self.state.check_threat(False)
            if result is not None:
                return result
        return best_move
