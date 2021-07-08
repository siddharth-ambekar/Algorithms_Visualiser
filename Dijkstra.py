import pygame
from collections import deque
import time

width=1300;
window1=pygame.display.set_mode((width,width));
window2=pygame.display.set_mode((width,width));
window3=pygame.display.set_mode((width,width));

BLACK=(0,0,0);
WHITE=(255,255,255);
GREEN=(0,255,0);
RED=(255,0,0);
BLUE=(0,0,255);
PURPLE=(128,0,128);
YELLOW=(255,215,0);

class Node(object):
	def __init__(self,row,col,width):
		self.neighbors={}; 
		self.colour=WHITE;
		self.x=col*width;
		self.y=row*width;
		self.width=width;
		self.row=row;
		self.col=col;

	def start(self):
		return self.colour==BLUE;

	def end(self):
		return self.colour==RED;

	def path(self):
		return self.colour==PURPLE;

	def front(self):
		return self.colour==YELLOW;

	def vis(self):
		return self.colour==GREEN;

	def nono(self):
		return self.colour==BLACK;

	def reset(self):
		self.colour=WHITE;

	def make_start(self):
		self.colour=BLUE;

	def make_end(self):
		self.colour=RED;

	def make_path(self):
		self.colour=PURPLE;

	def make_front(self):
		self.colour=YELLOW;

	def make_vis(self):
		self.colour=GREEN;

	def make_nono(self):
		self.colour=BLACK;

	def draw(self,window):
		pygame.draw.rect(window,self.colour,(self.y,self.x,self.width,self.width));

def make_grid(rows,width):
	grid=[];
	gap=width//rows;
	for i in range(rows):
		grid.append([]);
		for j in range(rows):
			n=Node(i,j,gap);
			grid[i].append(n);
	return grid;

def drawgrid(window,rows,width):
	gap=width//rows;
	for i in range(rows):
		pygame.draw.line(window,BLACK,(0,i*gap),(width,i*gap));
		for j in range(rows):
			pygame.draw.line(window,BLACK,(j*gap,0),(j*gap,width));

def draw(window,grid,rows,width):
	window.fill(WHITE);
	for row in grid:
		for node in row:
			node.draw(window);

	drawgrid(window,rows,width);
	pygame.display.update();


def mouseclick_pos(pos,rows,width):
	gap=width//rows;
	y,x=pos;

	row=y//gap;
	col=x//gap;

	return row,col;

def main1(window,width):

	started=False;
	run=True;

	Initial=None;
	Final=None;

	rows=50;

	grid=make_grid(rows,width);

	while run:
		draw(window,grid,rows,width);
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False;

			if started:
				continue;

			if pygame.mouse.get_pressed()[0]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				if not Initial:
					if node!=Final:
						Initial=node;
						Initial.make_start();
						grid[row][col]=Initial;
				if not Final:
					if node!=Initial:
						Final=node;
						Final.make_end();
						grid[row][col]=Final;
				
				elif node!=Initial and node!=Final:
					node.make_nono();
					grid[row][col]=node;


			elif pygame.mouse.get_pressed()[2]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				c=node.colour;
				if node==Initial:
					Initial.reset();
					Initial=None;
				elif node==Final:
					Final.reset();
					Final=None;
				else:
					if c==BLACK:
						node.reset();

			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_SPACE and not started:
					G=Create_Graph(grid,rows);
					s=(Initial.row,Initial.col);
					e=(Final.row,Final.col);
					BellmannFord(G,s,e,window,grid);
					started=True;
					run=False;


def main2(window,width):

	started=False;
	run=True;

	Initial=None;
	Final=None;

	rows=50;

	grid=make_grid(rows,width);

	while run:
		draw(window,grid,rows,width);
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False;

			if started:
				continue;

			if pygame.mouse.get_pressed()[0]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				if not Initial:
					if node!=Final:
						Initial=node;
						Initial.make_start();
						grid[row][col]=Initial;
				if not Final:
					if node!=Initial:
						Final=node;
						Final.make_end();
						grid[row][col]=Final;
				
				elif node!=Initial and node!=Final:
					node.make_nono();
					grid[row][col]=node;


			elif pygame.mouse.get_pressed()[2]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				c=node.colour;
				if node==Initial:
					Initial.reset();
					Initial=None;
				elif node==Final:
					Final.reset();
					Final=None;
				else:
					if c==BLACK:
						node.reset();

			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_SPACE and not started:
					G=Create_Graph(grid,rows);
					s=(Initial.row,Initial.col);
					e=(Final.row,Final.col);
					Dijkstra(G,s,e,window,grid);
					started=True;
					run=False;

def main3(window,width):

	started=False;
	run=True;

	Initial=None;
	Final=None;

	rows=50;

	grid=make_grid(rows,width);

	while run:
		draw(window,grid,rows,width);
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False;

			if started:
				continue;

			if pygame.mouse.get_pressed()[0]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				if not Initial:
					if node!=Final:
						Initial=node;
						Initial.make_start();
						grid[row][col]=Initial;
				if not Final:
					if node!=Initial:
						Final=node;
						Final.make_end();
						grid[row][col]=Final;
				
				elif node!=Initial and node!=Final:
					node.make_nono();
					grid[row][col]=node;


			elif pygame.mouse.get_pressed()[2]:
				pos=pygame.mouse.get_pos();
				row,col=mouseclick_pos(pos,rows,width);
				node=grid[row][col];
				c=node.colour;
				if node==Initial:
					Initial.reset();
					Initial=None;
				elif node==Final:
					Final.reset();
					Final=None;
				else:
					if c==BLACK:
						node.reset();

			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_SPACE and not started:
					G=Create_Graph(grid,rows);
					s=(Initial.row,Initial.col);
					e=(Final.row,Final.col);
					BFS(G,s,e,window,grid);
					started=True;
					run=False;


def Neighbours(r,c,grid,rows):
	l=[];
	try:
		if r!=0:
			n1=grid[r-1][c];
			if n1.colour!=BLACK:
				l.append((r-1,c));
	except IndexError:
		None;
	try:
		n2=grid[r+1][c];
		if n2.colour!=BLACK:
			l.append((r+1,c));
	except IndexError:
		None;
	try:
		if c!=0:
			n3=grid[r][c-1];
			if n3.colour!=BLACK:
				l.append((r,c-1));
	except IndexError:
		None;
	try:
		n4=grid[r][c+1];
		if n4.colour!=BLACK:
			l.append((r,c+1));
	except IndexError:
		None;
	return l;


def Create_Graph(grid,rows):
	G={};
	for row in grid:
		for node in row:
			if node.colour==BLACK:
				continue;
			else:
				r=node.row;
				c=node.col;
				if not G.get((r,c),False):
					G[(r,c)]={};
				l=Neighbours(r,c,grid,rows);
				for i in l:
					G[(r,c)].update(({i:1}));
	return G;

import copy

def BellmannFord(G,s,e,window,grid):
	if G.get(e,False) and G.get(s,False):
		P={i:float("Inf") for i in G};
		P[s]=0;
		l=len(G);
		alp={i:float("Inf") for i in G};
		alp[s]=0;
		for i in range(1,l+1):
			K=alp;
			K[s]=0;
			print(i,'\n');
			for node in G:
				if node==s:
					continue;
				else:
					if i==1:
						if G[s].get(node,False):
							K[node]=1;
							if node!=e:
								x=grid[node[0]][node[1]];
								if x.colour!=GREEN:
									x.make_vis();
									x.draw(window);
									pygame.display.update();
					else:
						N=G[node];
						S=[P[n]+1 for n in N];
						S.append(P[node]);
						K[node]=min(S);
						if P[node]<float("Inf"):
							if node!=e:
								x=grid[node[0]][node[1]];
								if x.colour!=GREEN:
									x.make_vis();
									x.draw(window);
									pygame.display.update();
			P=K;

		path=deque();
		end=e;
		count=0;
		while True:
			N=G[end];
			L=[(n,P[n]) for n in N];
			x=min(L,key=lambda q:q[1]);
			nod=x[0];
			u=grid[nod[0]][nod[1]];
			if nod==s:
				break;
			else:
				path.appendleft(nod);
				u.make_path();
				u.draw(window);
				pygame.display.update();
				end=nod;
		print(path);		

def Dijkstra(G,s,e,window,grid):
	if G.get(s,False) and G.get(e,False):
		P={i:float("Inf") for i in G};
		P[s]=0.0;
		V={i:False for i in G};
		V[s]=True;
		N=G[s];
		v=1;
		NODES=len(G);
		if len(N)==0:
			pygame.quit();
		else:
			frontier=[[s,n,1] for n in N];
			for n in N:
				if n!=e:
					x=grid[n[0]][n[1]];
					x.make_front();
					x.draw(window);
					pygame.display.update();

			while v<NODES:
				f=len(frontier);
				if f==0:
					break;
				else:
					edge=min(frontier,key=lambda x:x[2]);
					n1=edge[0];
					n2=edge[1];
					P[n2]=edge[2];
					V[n1]=True;
					V[n2]=True;
					if n2==e:
						break;
					if n1!=e and n1!=s:
						x=grid[n1[0]][n1[1]];
						x.make_vis();
						x.draw(window);
						pygame.display.update();
					if n2!=e and n2!=s:
						x=grid[n2[0]][n2[1]];
						x.make_front();
						x.draw(window);
						pygame.display.update();
					N=G[n2];
					if len(N)!=0:
						for n in N:
							if V[n]==False:
								frontier+=[[n2,n,P[n2]+1]];
					f=[];
					for edge in frontier:
						if V[edge[0]]==True and V[edge[1]]==True:
							pass;
						else:
							f+=[edge];
					frontier=f;
					v+=1;
	path=deque();
	end=e;
	count=0;
	while True:
		N=G[end];
		L=[(n,P[n]) for n in N];
		x=min(L,key=lambda q:q[1]);
		nod=x[0];
		u=grid[nod[0]][nod[1]];
		if nod==s:
			break;
		else:
			path.appendleft(nod);
			u.make_path();
			u.draw(window);
			pygame.display.update();
			end=nod;
	print(path);		

def BFS(G,s,e,window,grid):
	V={i:False for i in G};
	Q=deque();
	Q.append(s);
	P={i:0 for i in G};
	while True:
		if len(Q)==0:
			break;
		else:
			i=Q.popleft();
			if V[i]==True:
				None;
			else:
				x=grid[i[0]][i[1]];
				if i!=e and i!=s:
					x.make_vis();
					x.draw(window);
					pygame.display.update();
				V[i]=True;
				N=G[i];
				for n in N:
					if V[n]==False:
						Q.append(n);
						P[n]=P[i]+1;
						if n!=e and n!=s:
							X=grid[n[0]][n[1]];
							X.make_front();
							X.draw(window);
							pygame.display.update();
	path=deque();
	end=e;
	count=0;
	while True:
		N=G[end];
		L=[(n,P[n]) for n in N];
		x=min(L,key=lambda q:q[1]);
		nod=x[0];
		u=grid[nod[0]][nod[1]];
		if nod==s:
			break;
		else:
			path.appendleft(nod);
			u.make_path();
			u.draw(window);
			pygame.display.update();
			end=nod;
	print(path);
				
	
						

main1(window1,width);
time.sleep(8);
main2(window2,width);
time.sleep(8);
main3(window3,width);
time.sleep(5);
pygame.quit();
