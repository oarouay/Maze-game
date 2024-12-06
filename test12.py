from collections import deque
import random
import turtle

class Graphe:
    def __init__(self, L, C):
        self.L = L
        self.C = C
        self.graphe = {(0, 0): []}


    def ajouterNoeud(self, i, j):
        if (i, j) not in self.graphe.keys():
            self.graphe[(i, j)] = []

    def ajouterArc(self, c1, c2, porte=False):
        if c2 in self.graphe.keys() and c1 in self.graphe.keys() and ((c2),True) not in self.graphe[c1] and ((c2),False) not in self.graphe[c1] and ((c1),True) not in self.graphe[c2] and ((c1),False) not in self.graphe[c2] :
            self.graphe[c1].append((c2, porte))
            self.graphe[c2].append((c1, porte))

    def listerNoeuds(self):
        return self.graphe.keys()

    def listerArcs(self, c):
        if c not in self.graphe.keys():
            return self.graphe.values()

    def adjacenceNoeud(self, c1, c2):
        l = self.graphe[c1]
        return (c2, True) in l or (c2, False) in l

    def AfficherGraphe(self):
       for node in self.graphe:
           print(f"{node}->{self.graphe[node]}")
    
    def ajouterArcsVoisins(self):
        
        for i in range(self.L):
            for j in range(self.C):
                if i > 0:
                    self.ajouterArc((i, j), (i-1, j), random.choice([True, False]))
                if i < self.L - 1:
                    self.ajouterArc((i, j), (i+1, j), random.choice([True, False]))
                if j > 0:
                    self.ajouterArc((i, j), (i, j-1), random.choice([True, False]))
                if j < self.C - 1:
                    self.ajouterArc((i, j), (i, j+1), random.choice([True, False]))
    def AfficherLabyrinthe(self):
        a=SearchLabyrinthe(self.graphe)
        turtle.speed(0)
        taille_case = 30
        path_fouded=[(self.L-1,self.C-1)]
        for i in a.depth_first_search((0,0),(self.C-1,self.L-1)):
            path_fouded.append(i)
        
        col="#ADD8E6"

        for i in range(self.L):  
            for j in range(self.C): 
                x = j * taille_case-120
                y = -i * taille_case+100
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                if (i,j) in path_fouded:
                    turtle.fillcolor(col)
                    turtle.begin_fill()
                if(not has_box_above(self.C,i,j)):
                    turtle.setheading(0)
                    turtle.forward(taille_case)
                else:
                    if ((i-1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(0)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(0)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_right(self.C,i,j)):
                    turtle.setheading(-90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j+1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(-90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(-90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_below(self.C,i,j)):
                    turtle.setheading(180)
                    turtle.forward(taille_case)
                else:
                    if ((i+1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(180)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(180)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_left(self.C,i,j)):
                    turtle.setheading(90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j-1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                if (i,j) in path_fouded:
                    turtle.end_fill()
                
        turtle.hideturtle()
        turtle.done()
    def random_lab(self,start,goal):
        a=SearchLabyrinthe(self.graphe)
        for i in range(l):
            for j in range(c):
                self.ajouterNoeud(i, j)
        t=None
        while t==None :
            self.graphe = {(0, 0): []}
            for i in range(l):
                for j in range(c):
                    self.ajouterNoeud(i, j)            
            self.ajouterArcsVoisins()
            t=a.breadth_first_search(start,goal)
              
    

class SearchLabyrinthe:
    def __init__(self,g):
        self.graph =g
        self.explored = {}
        self.accessible = {}
    def successeur(self,k):
        l=[]
        for i in g.graphe[k]:
            if i[1]==True:
                l.append(i[0])
        return l
    def breadth_first_search(self,start,goal):
        file=deque()
        file.append(start)
        exploree=[start]
        accessible={}
        while(len(file)>0):
            x=file.popleft()
            if(goal not in accessible):
                for voisin in self.successeur(x):
                    if voisin not in exploree:
                        accessible[voisin]=x
                        file.append(voisin)
                        exploree.append(voisin)
                    
        chemin={}
        noeud=goal
        while noeud!=(0,0):
            try:
                chemin[accessible[noeud]]=noeud
                noeud=accessible[noeud]
            except:
                print('nexiste pas!')
                return None
        return chemin
    def depth_first_search(self,start,goal):
        pile=deque()
        pile.append(start)
        exploree=[start]
        accessible={}
        while(len(pile)>0):
            x=pile.pop()
            if(goal not in accessible):
                for voisin in self.successeur(x):
                    if voisin not in exploree:
                        accessible[voisin]=x
                        pile.append(voisin)
                        exploree.append(voisin)
                    
        chemin={}
        noeud=goal
        while noeud!=(0,0):
            try:
                chemin[accessible[noeud]]=noeud
                noeud=accessible[noeud]
            except:
                print('nexiste pas!')
                return None
        return chemin
    def __init__(self,g):
        self.graph =g
        self.explored = {}
        self.accessible = {}

    def successeurs(self, current_state):
        return [x[0] for x in self.graph.listerArcs(current_state) if x[1]]

    def VerifEtat(self, state):
        return not (state in self.explored.keys()  or state in self.accessible.keys())

    def succValide(self, current_state):
        return [x[0] for x in self.graph.listerArcs(current_state) if x[1] and self.VerifEtat(x[0])]

def has_box_above(l, row, col):
    if row == 0:
        return False
    else:
        return True

def has_box_below(l, row, col):
    if row == l - 1:
        return False
    else:
        return True

def has_box_left(c, row, col):
    if col == 0:
        return False
    else:
        return True

def has_box_right(c, row, col):
    if col == c - 1:
        return False
    else:
        return True


l=10
c=10
g = Graphe(l, c)

g.random_lab((0,0),(l-1,c-1))
g.AfficherGraphe()
g.AfficherLabyrinthe()


