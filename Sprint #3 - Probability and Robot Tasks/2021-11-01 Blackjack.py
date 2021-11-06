#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[81]:


def initial_state():
    
    deck=makedeck()
    
    player1_hand=deal(deck,1)
    player2_hand=deal(deck,1)
    player1_stay=player2_stay=False
    
    return [player1_hand,player2_hand,deck,player1_stay,player2_stay]
    


# In[82]:


def score(hand):
    total=0
    has_ace=False
    for card in hand:
        if card.rank>10:
            total+=10
        else:
            total+=card.rank
        if card.rank==1:
            has_ace=True
            
    if has_ace and total+10<=21:
        return total+10
    else:
        return total
    


# In[83]:


def show_state(state):
    hand1,hand2,deck,p1_stay,p2_stay=state
    
    player=1
    if player==1:
        other_player=2
    else:
        other_player=1
        
    print(f"Player {player} hand is {hand1} (score {score(hand1)})",end="")
    if p1_stay:
        print("-- Staying.")
    else:
        print()
    
    print(f"Player {other_player} hand is {hand2} (score {score(hand2)})")
    if p2_stay:
        print("-- Staying.")
    else:
        print()
    


# In[84]:


show_state(initial_state())


# In[85]:


def valid_moves(state,player):
    return ["hit","stay"]


# In[86]:


def update_state(state,player,move):
    new_state=state
    hand1,hand2,deck,p1_stay,p2_stay=state
    
    if move=="stay":
        if player==1:
            new_state[3]=True
        else:
            new_state[4]=True            
        
        return state
    
    assert move=='hit',f"You can't get there from here: {move}"
    
    # hit
    
    if player==1:
        hand1+=deal(deck,1)
    else:
        hand2+=deal(deck,1)
        
    new_state=[hand1,hand2,deck,p1_stay,p2_stay]
    return new_state
    


# In[87]:


def win_status(state,player):
    hand1,hand2,deck,p1_stay,p2_stay=state
    
    score1=score(hand1)
    score2=score(hand2)
    
    if p1_stay and p2_stay:
        if player==1:
            if score1>score2:
                return "win"
            elif score1==score2:
                return "stalemate"
            else:
                return "lose"
        else:
            if score2>score1:
                return "win"
            elif score1==score2:
                return "stalemate"
            else:
                return "lose"
            
    if player==1 and score1>21:
        return "lose"

    if player==2 and score2>21:
        return "lose"
    
    if p2_stay and score1>score2:
        if player==1:
            return "win"
        else:
            return "lose"
    
    if p1_stay and score2>score1:
        if player==1:
            return "lose"
        else:
            return "win"
    


# In[88]:


def repeat_move(state,player,move):
    hand1,hand2,deck,p1_stay,p2_stay=state
    
    if player==1 and p2_stay:
        return True
    
    if player==2 and p1_stay:
        return True
    
    return False # all other cases


# In[89]:


def human_move(state,player):
    while True:
        move=input(f"Player {player}: Hit or stay?").lower()

        if move[0]=='h':
            return "hit"
        elif move[0]=='s':
            return "stay"

        print("Bad Move")
        
human_agent=Agent(human_move)


# In[91]:


g=Game()
g.run(human_agent,human_agent)


# In[ ]:




