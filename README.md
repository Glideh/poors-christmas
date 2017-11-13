# Poors Christmas

Do

```
$ docker-compose up
```

And you will see each participants found in `app/participants.yml` given a random other participant as target (so he can give him a present).

## Rules

A participant can't gift:

* Himself
* Someone from the same group
* Someone already having a gifter
* Someone he gifted in the past already

## Example

Participant files:

```yml
participants:
  - { name: 'Participant 1', group: 1 }
  - { name: 'Participant 2', group: 1 }
  - { name: 'Participant 3' }
  - { name: 'Participant 4', group: 2 }
  - { name: 'Participant 5', group: 2, history: ['Participant 2'] }
  - { name: 'Participant 7', group: 3, history: ['Participant 3'] }
  - { name: 'Participant 6', group: 3 }
```

```
$ docker-compose up
```

Output:

> Participant 1 => Participant 3  
Participant 2 => Participant 4  
Participant 3 => Participant 1  
Participant 4 => Participant 2  
Participant 5 => Participant 6  
Participant 6 => Participant 7  
Participant 7 => Participant 5
