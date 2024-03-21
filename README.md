# ram-machine

Un programme pour exécuter des programmes RAM en Python.

### Utilisation

```shell
python main.py <fichier> [r0] [r1] ... [rn]
```

### Exemple d'utilisation

```shell
python main.py programs/add.ram 5 3
```

### Fonctionnement

Une machine RAM est constituée

- De registres r0, r1, ..., rn contenant des entiers
- D'une suite finie numérotée d'instructions de 5 types possibles:
  - **copy ri rj**: copie la valeur de rj dans ri
  - **inc ri**: incrémente la valeur de ri
  - **dec ri**: décrémente la valeur de ri
  - **jump ri l**: saute à l'instruction à la ligne l si ri vaut 0
  - **stop**: arrête le programme

On met les entrées (données en argument du programme) dans r0, r1, ..., rn. Les registres non utilisés sont initialisés à 0.  
Le programmeur doit mettre les sorties (résultats) dans r0, r1, ..., rn.

### Exemple de programme

Programme qui renvoie 1 si r0 == r1, 0 sinon.  
Le résultat est stocké dans r0.

```
jump r0 5
dec r0
dec r1
jump r2 1
jump r1 7
stop
inc r0
stop
```

Il ne reste plus qu'à l'exécuter:

```shell
python main.py programs/equals.ram 5 5
```
