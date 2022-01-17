def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    cur_weight = 0

    while truck_weights:
        answer += 1
        cur_weight -= bridge.pop(0)
        if cur_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            cur_weight += truck

    print(bridge, cur_weight)

    while cur_weight > 0:
        answer += 1
        cur_weight -= bridge.pop(0)

    return answer
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = []

#     while truck_weights or bridge:
#         if len(bridge) > 0 and answer >= bridge_length:
#             bridge.pop(0)

#         answer += 1
#         while truck_weights and truck_weights[0]+sum(bridge) <= weight and len(bridge) < bridge_length:
#             bridge.append(truck_weights.pop(0))
#             answer += 1


#     return answer
