#będziemy używali networkx
#strona pomocnicza https://networkx.org/documentation/stable/tutorial.html

import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from PIL import Image
import os

def random_graph(n = 10, p = 0.3):
    """
    Opis:  
        Funkcja która:
            1. za pomocą biblioteki networkx tworzy losowy graf o n wierzchołkach i rysuje połączenia między 
            nimi z prawdopodobieństwem wystąpienia p
            2. tworzy animację błądzenia agenta po grafie, wybiera jeden losowy wierzchołek jako punkt startowy,
             oznacza go kolorem pomarańczowym, po czym wybiera losowo jednego sąsiada i przenosi się tam, zaznaczając
             go kolorem pomarańczowym, jedno przejście oznacza jedną klatkę animacji

    Argumenty:
        n : int 
            określa:
                - ilość wierzchołków które zostaną narysowane na grafie (domyślnie 10)
                - ilość klatek animacji +1
                
        p : float
            określa prawdopodobieństwo wystąpienia połączenia pomiędzy dwoma wierzchołkami, ułamek między 0 i 1 (domyślnie 0.3)

    Zwraca:
        Plik gif zapisany w katalogu programu przedstawiający błądzenie agetna po grafie        
    
    """    
    G = nx.Graph()                                              #stwarzamy graf
    G.add_nodes_from(range(n))                                  #dodajemy elementy do grafa(nodes)                                  
    
    #teraz stworzymy połączenia, każde połączenie ma p szansy na powstanie, gdzie 0 < p < 1
    #szybko wygenerujmy wszystkie możliwe połączenia(bez powtarzania się)

    edges = [(i,j) if i<j  else 0 for i in range(n) for j in range(n)]
    while edges.count(0)>0:
        edges.remove(0)

    #dodajemy połączenia z szansą p
    for edge in edges:
        if rand.randint(1,100) < p*100:
            G.add_edge(*edge)

    #pobieramy pozycję elementówn na grafie(potrzebne do rysowania)
    pos = nx.layout.random_layout(G)             
    
    #tworzymy kanvas
    ax = plt.subplot()     


    #wybór losowego elementu
    agent = rand.choice(list(G.nodes))
    without_agent = list(G.nodes)
    without_agent.remove(agent) 


    nx.draw_networkx_nodes(G,pos, nodelist=[agent], node_color="tab:orange")            #rysujemy nasz "aktywny" element
    nx.draw_networkx_nodes(G,pos, nodelist=without_agent, node_color="tab:blue")        #rysujemy resztę
    
    nx.draw_networkx_labels(G,pos)                                                      #dodajemy podpisy
    
    nx.draw_networkx_edges(G, pos)                                                      #dodajemy połączenia
    
    plt.savefig("zdj_bldz_lsw\\fig0.png")

    #tworzymy pętlę wybierającą kolejne miejsce agenta z sąsiadów agenta, po czym przerysowywuje canvas z nową pozycją
    n = 20 #ilość klatek
    for i in range(1,n+1):

        adj = list(G.adj[agent].keys())                                                     #sąsiedzi naszego losowego agenta    
        
        agent = rand.choice(adj)
        without_agent = list(G.nodes)
        without_agent.remove(agent) 

        nx.draw_networkx_nodes(G,pos, nodelist=[agent], node_color="tab:orange")            #rysujemy nasz "aktywny" element
        nx.draw_networkx_nodes(G,pos, nodelist=without_agent, node_color="tab:blue")        #rysujemy resztę
        
        nx.draw_networkx_labels(G,pos)                                                      #dodajemy podpisy
        
        nx.draw_networkx_edges(G, pos)                                                      #dodajemy połączenia
        
        plt.savefig("zdj_bldz_lsw\\fig"+str(i)+".png")


    #tworzenie gifa
    pictures = ["zdj_bldz_lsw\\fig"+str(i)+".png" for i in range(0,n+1)]
    frames = [Image.open(image) for image in pictures]
    frame_one = frames[0]
    frame_one.save("chodzący_agent.gif", format="GIF", append_images = frames, save_all=True, duration=n*30, loop=0)

    #usuwamy zdjęcia potrzebne do gifa
    folder = os.path.join(os.getcwd(),"zdj_bldz_lsw")
    for filename in os.listdir(folder):
        filepath = os.path.join(folder,filename)
        os.remove(filepath)


# ==============================================================================================================================================================
def watts_strogatz_graph(n = 10, k = 2 ,p = 0.5):
    """
    Opis:  
        Funkcja która za pomocą biblioteki networkx generuje gotowy graf Watts-a Strogatz-a, a następnie tworzy
        animację przemieszczania się agenta po tym grafie.

    Argumenty:
        n : int 
            określa:
                - ilość wierzchołków które zostaną narysowane na grafie (domyślnie 10)
                - ilość klatek animacji +1

        k : int
            określa ilość sąsiadów z jaką zostanie połączony każdy wierzchołek, jeśli k to liczba nieparzysta,
            to bierze k-1
                
        p : float
            określa prawdopodobieństwo zamiany istniejącego połączenia pomiędzy dwoma sąsiednimi wierzchołkami,
            na połączenie z losowym innym wierzchołkiem

    Zwraca:
        Plik gif zapisany w katalogu programu przedstawiający błądzenie agetna po grafie Watts-a Strogatz-a   
    
    """  
    G = nx.watts_strogatz_graph(n,k,p)
    pos = nx.spring_layout(G)

    
    ax = plt.subplot()     
    
    #stwarzamy własną listę kolorów
    my_node_list_colors=["blue" for el in G.nodes]

    #wybór losowego elementu
    agent = rand.choice(list(G.nodes))

    my_node_list_colors[agent] = "orange"



   
    nx.draw_networkx_nodes(G,pos,node_color=my_node_list_colors)            #rysujemy nasz graf z aktywnym elementem
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    plt.savefig("zdj_bldz_lsw\\fig0.png")

    #ZMIANA AGENTA
    for i in range(1,n+1):
        stary_agent = agent
        adj = list(G.adj[agent].keys())                                                   #sąsiedzi naszego losowego agenta     
        agent = rand.choice(adj)                                                          #nowy agent

        my_node_list_colors[stary_agent]="blue"
        my_node_list_colors[agent]="orange"

        nx.draw_networkx_nodes(G,pos,node_color=my_node_list_colors)            #rysujemy nasz graf z aktywnym elementem
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        
        plt.savefig("zdj_bldz_lsw\\fig"+str(i)+".png")
        plt.clf()


    #tworzenie gifa
    pictures = ["zdj_bldz_lsw\\fig"+str(i)+".png" for i in range(0,n+1)]
    frames = [Image.open(image) for image in pictures]
    frame_one = frames[0]
    frame_one.save("chodzący_agent_watts_strogatz_graph.gif", format="GIF", append_images = frames, save_all=True, duration=n*30, loop=0)

    #usuwamy zdjęcia potrzebne do gifa
    folder = os.path.join(os.getcwd(),"zdj_bldz_lsw")
    for filename in os.listdir(folder):
        filepath = os.path.join(folder,filename)
        os.remove(filepath)
    




def barabasi_albert_graph(n=15,k=2):
    """
    Opis:  
        Funkcja która za pomocą biblioteki networkx generuje gotowy graf Barabasi-Alberta, a następnie tworzy
        animację przemieszczania się agenta po tym grafie.

    Argumenty:
        n : int 
            określa:
                - ilość wierzchołków które zostaną narysowane na grafie (domyślnie 15)
                - ilość klatek animacji +1

        k : int
            określa ilość połączeń, do połączenia nowszych wierzchołków z istniejącymi (domyślnie 2)
                

    Zwraca:
        Plik gif zapisany w katalogu programu przedstawiający błądzenie agetna po grafie Watts-a Strogatz-a   
    
    """

    G = nx.barabasi_albert_graph(n,k)
    pos = nx.spring_layout(G)

    ax = plt.subplot()     
    
    #stwarzamy własną listę kolorów
    my_node_list_colors=["blue" for el in G.nodes]

    #wybór losowego elementu
    agent = rand.choice(list(G.nodes))

    #w tablicy kolorów w miejsce odpowiadajęcemu aktywnemu agentowi przypisuje wyróżniający kolor
    my_node_list_colors[agent] = "orange"

    nx.draw_networkx_nodes(G,pos,node_color=my_node_list_colors)            #rysujemy nasz graf 
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    plt.savefig("zdj_bldz_lsw\\fig0.png")

    
    #ZMIANA AGENTA
    for i in range(1,n+1):
        stary_agent = agent
        adj = list(G.adj[agent].keys())                                                   #sąsiedzi naszego losowego agenta     
        agent = rand.choice(adj)                                                          #nowy agent

        #zaznaczamy kolor nowego agenta na pomarańczowy, starego znowu na niebieski
        my_node_list_colors[stary_agent]="blue"
        my_node_list_colors[agent]="orange"

        nx.draw_networkx_nodes(G,pos,node_color=my_node_list_colors)            #rysujemy nasz graf z aktywnym elementem
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        
        plt.savefig("zdj_bldz_lsw\\fig"+str(i)+".png")
        plt.clf()


    #tworzenie gifa
    pictures = ["zdj_bldz_lsw\\fig"+str(i)+".png" for i in range(0,n+1)]
    frames = [Image.open(image) for image in pictures]
    frame_one = frames[0]
    frame_one.save("chodzący_agent_barabasi_albert_graph.gif", format="GIF", append_images = frames, save_all=True, duration=n*30, loop=0)

    #usuwamy zdjęcia potrzebne do gifa
    folder = os.path.join(os.getcwd(),"zdj_bldz_lsw")
    for filename in os.listdir(folder):
        filepath = os.path.join(folder,filename)
        os.remove(filepath)
    

#random_graph(15,0.2)
#watts_strogatz_graph(10,4,0)
barabasi_albert_graph(15,2)
