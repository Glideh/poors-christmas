# Poors Christmas

Do

```
$ docker-compose up
```

And you will see each participants found in `app/participants.yml` given a random other participant as target (so he can give him a present).

## Example

Participant files:

```yml
participants:
  - { name: 'Participant 1', group: 1 }
  - { name: 'Participant 2', group: 1 }
  - { name: 'Participant 3' }
  - { name: 'Participant 4', group: 2 }
  - { name: 'Participant 5', group: 2 }
  - { name: 'Participant 6', group: 3 }
  - { name: 'Participant 7', group: 3 }
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
