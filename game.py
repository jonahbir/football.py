

def main_func(input1,colors):
    non_home=0

    for i in range(input1):
        index=0
        while index<input1:
            if i!=index:
                host=colors[i]
                invited=colors[index]
                home_host,guest_host=host
                home_invited,guest_invited=invited
                if home_host==guest_invited:
                    non_home+=1
            index+=1
    return non_home 

input1=int(input())
colors=[]
for i in range(input1):
    teamc=tuple(map(int, input().split()))
    colors.append(teamc)
print(main_func(input1,colors))
