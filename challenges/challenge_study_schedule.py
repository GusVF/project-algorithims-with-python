permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 4

# criar uma constante para armazenar o resultado
# percorrer a lista
# verificar se os itens da lista e 'target_time' sao 'integers'
# verificar quantas vezes o target_time aparece entre start_time/end_time
# o numero que aparece mais vezes e o melhor horario.


def study_schedule(permanence_period: list[tuple], target_time: int):
    best_time = 0
    for start_time, end_time in permanence_period:
        if not (
            isinstance(start_time, int)
            and isinstance(end_time, int)
            and isinstance(target_time, int)
        ):
            return None
        if start_time <= target_time <= end_time:
            best_time += 1
    return best_time

    # raise NotImplementedError


result = study_schedule(permanence_period, target_time)
print(result)
