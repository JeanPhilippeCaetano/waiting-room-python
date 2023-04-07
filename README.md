# <p align="center">Projet waiting-room-python
</p>
  
Ce projet waiting-room-python est un système simple de gestion de patients et de médecins. Il nous permet de consulter, d'ajouter, de mettre à jour et de supprimer des patients, ainsi que de trouver le patient le plus urgent pour consultation.


  
## 🛠️ Install Dependencies    
Clonez le repository : git clone https://github.com/JeanPhilippeCaetano/waiting-room-python.git    
    
Déplacez-vous dans le dossier :
```bash
cd waiting-room-python
```
Installez les dépendances : 
```bash
pip install -r flask
```
```bash
pip install -r request
```
```bash
pip install -r jsonify
```

## 🧐 Features    
- GET /get-patient/int:patient_id Récupère un patient à partir de son identifiant.
- GET /get-patient/int:patient_id Récupère un patient à partir de son identifiant.
- GET /get-patient/int:patient_id Récupère un patient à partir de son identifiant.
- POST /add-patient Ajoute un nouveau patient à la liste des patients.
- GET /get-most-urgent-patient Récupère le patient le plus urgent pour consultation.
- PUT /update-patient/int:patient_id Met à jour les informations d'un patient existant.
- DELETE /delete-patient/int:id Supprime un patient existant à partir de son identifiant.
- POST /add-doctor Ajoute un nouveau médecin à la liste des médecins.
- GET /get-doctor/int:doctor_id Récupère un médecin à partir de son identifiant.
- PUT /update-doctor/int:doctor_id Met à jour les informations d'un médecin existant.
- DELETE /delete-doctor/int:id Supprime un médecin existant à partir de son identifiant.




## 🙇 Author
#### CAETANO Jean-Philippe
- Github: https://github.com/JeanPhilippeCaetano
        
#### SAIOUDI Wassim
- Github: https://github.com/2va2s
 
#### THOYER Gabby
- Github: https://github.com/sebtick
 
 #### SEGURET Emile
- Github: https://github.com/Spikesito
