#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[20]:


def initial_state():
    
    deck=makedeck()
    
    player1_hand=deal(deck,2)
    player2_hand=deal(deck,2)
    player1_stay=player2_stay=False
    
    return [player1_hand,player2_hand,deck,player1_stay,player2_stay,None,None]
    


# In[21]:


def score(hand):
    total=0
    has_ace=False
    for card in hand:
        if card is None:
            continue
        
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
    


# In[22]:


def state_to_observation(state,player):
    hand1,hand2,deck,p1_stay,p2_stay,last_card1,last_card2=state
    
    if player==1:
        observation=hand1,hand2[1:],p1_stay,p2_stay,last_card1,last_card2 # only the 2nd and further card
    else:
        observation=hand2,hand1[1:],p2_stay,p1_stay,last_card2,last_card1  # only the 2nd and further card
        
    return observation


# In[23]:


def show_state(observation):
    hand1,hand2,player_stay,opponent_stay,last_card1,last_card2=observation

    if last_card1:
        print(f"Player last card dealt: {last_card1}")
    print(f"Player hand is {hand1} (score {score(hand1)})",end="")
    if player_stay:
        print("-- Staying.")
    else:
        print()
    
    if last_card2:
        print(f"Opponent last card dealt: {last_card2}")
    print(f"Opponent hand showing is {hand2} (showing score {score(hand2)})")
    if opponent_stay:
        print("-- Staying.")
    else:
        print()
    


# In[24]:


show_state(state_to_observation(initial_state(),1))


# In[25]:


def valid_moves(state,player):
    return ["hit","stay"]


# In[26]:


def update_state(state,player,move):
    new_state=state
    hand1,hand2,deck,p1_stay,p2_stay,last_card1,last_card2=state
    
    if move=="stay":
        if player==1:
            new_state[3]=True
        else:
            new_state[4]=True            
        
        return state
    
    assert move=='hit',f"You can't get there from here: {move}"
    
    # hit
    
    if player==1:
        last_card1=deck.deal(1)[0]
        hand1+=[last_card1]
    else:
        last_card2=deck.deal(1)[0]
        hand2+=[last_card2]
        
    new_state=[hand1,hand2,deck,p1_stay,p2_stay,last_card1,last_card2]
    return new_state
    


# In[31]:


def win_status(state,player):
    hand1,hand2,deck,p1_stay,p2_stay,last_card1,last_card2=state
    
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
    
    # when there are cards not shown, then you don't want this extra logic to the game
#     if p2_stay and score1>score2:
#         if player==1:
#             return "win"
#         else:
#             return "lose"
    
#     if p1_stay and score2>score1:
#         if player==1:
#             return "lose"
#         else:
#             return "win"
    


# In[32]:


def repeat_move(state,player,move):
    hand1,hand2,deck,p1_stay,p2_stay,last_card1,last_card2=state
    
    if player==1 and p2_stay:
        return True
    
    if player==2 and p1_stay:
        return True
    
    return False # all other cases


# In[33]:


def human_move(observation,player):
    while True:
        move=input(f"Player {player}: Hit or stay?").lower()

        if move[0]=='h':
            return "hit"
        elif move[0]=='s':
            return "stay"

        print("Bad Move")
        
human_agent=Agent(human_move)


# In[36]:


g=Game()
g.run(human_agent,human_agent)


# In[19]:


human_agent.states


# In[ ]:




