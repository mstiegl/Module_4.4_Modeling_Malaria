import matplotlib.pyplot as plt
simLength=200  #days
dt = 0.0625
t=0
uninfected_humans=300
human_hosts=1
immune=0
uninfected_mosquitoes=300
vectors=0
mosquitos=uninfected_mosquitoes+vectors
prob_vector=vectors/mosquitos
deceased_humans=0
recovered=0
immunity_rate=0.01
malaria_induced_death_rate=0.005

recovery_rate=0.3
prob_bit=0.3
deceased_vectors=0
mosquito_death_rate=0.01
mosquito_birth_rate=0.01

flow_to_immune=immunity_rate * human_hosts
deceased_humans=malaria_induced_death_rate * human_hosts
recovered= recovery_rate * human_hosts
flow_to_host=prob_bit*prob_vector*uninfected_humans

mosquito_births=mosquito_birth_rate*(vectors+uninfected_mosquitoes)
humans=human_hosts+uninfected_humans+immune
prob_host=human_hosts/humans
infected_mosquitoes=prob_bit*prob_host*uninfected_mosquitoes
uninfected_mosquito_deaths=mosquito_death_rate*uninfected_mosquitoes
vector_deaths=mosquito_death_rate*vectors




vectorsLst=[vectors]
hostLst=[human_hosts]
uninfected_humansLst=[uninfected_humans]
immuneLst=[immune]
uninfected_mosquitoesLst=[uninfected_mosquitoes]
timeLst=[t]

while t<200:
    t=t+dt
    uninfected_humans=uninfected_humans+(recovered-flow_to_host)*dt
    vectors=vectors+(infected_mosquitoes-vector_deaths)*dt
    uninfected_mosquitoes=uninfected_mosquitoes+(mosquito_births-infected_mosquitoes-uninfected_mosquito_deaths)*dt
    human_hosts=human_hosts+(flow_to_host-flow_to_immune-recovered-deceased_humans)*dt
    immune=immune+flow_to_immune*dt
    mosquitos = uninfected_mosquitoes + vectors
    prob_vector = vectors / mosquitos
    recovered=human_hosts*recovery_rate
    flow_to_host = prob_bit * prob_vector * uninfected_humans
    flow_to_immune = immunity_rate * human_hosts
    deceased_humans = malaria_induced_death_rate * human_hosts
    mosquito_births = mosquito_birth_rate * (vectors + uninfected_mosquitoes)
    humans = human_hosts + uninfected_humans + immune
    prob_host = human_hosts / humans
    infected_mosquitoes = prob_bit * prob_host * uninfected_mosquitoes
    uninfected_mosquito_deaths = mosquito_death_rate * uninfected_mosquitoes
    vector_deaths = mosquito_death_rate * vectors

    vectorsLst.append(vectors)
    hostLst.append(human_hosts)
    uninfected_humansLst.append(uninfected_humans)
    immuneLst.append(immune)
    uninfected_mosquitoesLst.append(uninfected_mosquitoes)
    timeLst.append(t)
plt.plot(timeLst,vectorsLst,'g')
plt.text(125,280, 'Vectors', color='g')
plt.plot(timeLst, hostLst,'b')
plt.text(50,90, 'Hosts', color='b')
plt.plot(timeLst, uninfected_humansLst,'r')
plt.text(30,280, 'Uninfected_human', color='r')
plt.plot(timeLst, immuneLst, color='orange')
plt.text(175,100, 'Immune', color='orange')
plt.plot(timeLst, uninfected_mosquitoesLst,color='purple')
plt.text(100,10, 'Uninfected mosquitoes', color='purple')
plt.show()
