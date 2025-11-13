# characters.py - Données des personnages et classes D&D

character_classes = [
    {
        "name": "Guerrier",
        "description": "Un combattant robuste et courageux, maître des armes et de l'armure lourde.",
        "stats": {"Force": 16, "Dextérité": 12, "Constitution": 15, "Intelligence": 10, "Sagesse": 13, "Charisme": 11},
        "special_abilities": ["Attaque puissante", "Résistance aux dégâts", "Intimidation"],
        "weapon": "Épée longue",
        "armor": "Armure de plaques"
    },
    {
        "name": "Mage",
        "description": "Un érudit mystique capable de manipuler les forces magiques de l'univers.",
        "stats": {"Force": 8, "Dextérité": 14, "Constitution": 12, "Intelligence": 17, "Sagesse": 15, "Charisme": 13},
        "special_abilities": ["Boule de feu", "Téléportation", "Bouclier magique"],
        "weapon": "Bâton de pouvoir",
        "armor": "Robe de mage"
    },
    {
        "name": "Voleur",
        "description": "Un acrobate agile et discret, expert en furtivité et en crochetage de serrures.",
        "stats": {"Force": 11, "Dextérité": 17, "Constitution": 13, "Intelligence": 14, "Sagesse": 12, "Charisme": 10},
        "special_abilities": ["Attaque sournoise", "Furtivité", "Crochetage"],
        "weapon": "Dagues doubles",
        "armor": "Armure de cuir"
    },
    {
        "name": "Clerc",
        "description": "Un serviteur divin capable de guérir les blessures et de repousser les morts-vivants.",
        "stats": {"Force": 13, "Dextérité": 10, "Constitution": 14, "Intelligence": 12, "Sagesse": 16, "Charisme": 15},
        "special_abilities": ["Guérison", "Repousser morts-vivants", "Bénédiction"],
        "weapon": "Masse de guerre",
        "armor": "Cotte de mailles"
    },
    {
        "name": "Rôdeur",
        "description": "Un gardien de la nature, expert en survie et en combat à distance.",
        "stats": {"Force": 14, "Dextérité": 16, "Constitution": 13, "Intelligence": 12, "Sagesse": 15, "Charisme": 10},
        "special_abilities": ["Tir précis", "Communication avec animaux", "Survie"],
        "weapon": "Arc long",
        "armor": "Armure de cuir cloutée"
    }
]

welcome_messages = {
    "Guerrier": (
        "Bienvenue, noble Guerrier ! Vous vous trouvez dans la taverne 'Le Dragon Doré' "
        "dans la ville de Valdris. Des rumeurs parlent d'un ancien donjon découvert dans les montagnes "
        "au nord, rempli de trésors mais aussi de dangers mortels. "
        "Plusieurs aventuriers ont déjà tenté de l'explorer, mais aucun n'est revenu...\n\n"
        "Que souhaitez-vous faire ?\n\n"
        "1. Demander des informations sur le donjon au tavernier\n"
        "2. Approcher un groupe d'aventuriers pour former une équipe\n"
        "3. Partir immédiatement vers le donjon en solitaire"
    ),
    "Mage": (
        "Bienvenue, sage Mage ! Vous vous trouvez dans la taverne 'Le Dragon Doré' "
        "dans la ville de Valdris. Des rumeurs parlent d'un ancien donjon découvert dans les montagnes "
        "au nord, rempli de trésors magiques mais aussi de créatures mystiques dangereuses. "
        "Vos études vous ont appris que ce donjon pourrait contenir des artefacts de pouvoir immense...\n\n"
        "Que souhaitez-vous faire ?\n\n"
        "1. Étudier les anciens textes sur ce donjon\n"
        "2. Rechercher des informations magiques auprès des érudits locaux\n"
        "3. Partir explorer le donjon pour découvrir ses secrets magiques"
    ),
    "Voleur": (
        "Bienvenue, discret Voleur ! Vous vous trouvez dans la taverne 'Le Dragon Doré' "
        "dans la ville de Valdris. Des rumeurs parlent d'un ancien donjon découvert dans les montagnes "
        "au nord, rempli de trésors précieux mais aussi de pièges mortels. "
        "Vos contacts vous ont appris que ce donjon contient des coffres remplis d'or et de bijoux...\n\n"
        "Que souhaitez-vous faire ?\n\n"
        "1. Écouter les conversations pour obtenir des informations\n"
        "2. Trouver un guide local qui connaît les pièges\n"
        "3. Partir en infiltration pour récupérer les trésors"
    ),
    "Clerc": (
        "Bienvenue, pieux Clerc ! Vous vous trouvez dans la taverne 'Le Dragon Doré' "
        "dans la ville de Valdris. Des rumeurs parlent d'un ancien donjon découvert dans les montagnes "
        "au nord, rempli de trésors sacrés mais aussi de morts-vivants maléfiques. "
        "Vos visions divines vous ont montré que ce donjon abrite une profanation qui doit être purifiée...\n\n"
        "Que souhaitez-vous faire ?\n\n"
        "1. Prière pour obtenir des conseils divins\n"
        "2. Rechercher des informations sur les créatures maléfiques\n"
        "3. Partir purifier le donjon des forces du mal"
    ),
    "Rôdeur": (
        "Bienvenue, sage Rôdeur ! Vous vous trouvez dans la taverne 'Le Dragon Doré' "
        "dans la ville de Valdris. Des rumeurs parlent d'un ancien donjon découvert dans les montagnes "
        "au nord, rempli de trésors naturels mais aussi de bêtes sauvages dangereuses. "
        "Vos sens vous ont alerté que ce donjon perturbe l'équilibre naturel de la région...\n\n"
        "Que souhaitez-vous faire ?\n\n"
        "1. Communiquer avec les animaux locaux pour obtenir des informations\n"
        "2. Étudier les traces et signes dans la nature\n"
        "3. Partir explorer le donjon pour restaurer l'équilibre naturel"
    )
}

def get_character_by_name(name):
    """Retourne les données d'un personnage par son nom"""
    for char in character_classes:
        if char["name"].lower() == name.lower():
            return char
    return None

def get_welcome_message(character_name):
    """Retourne le message de bienvenue pour une classe donnée"""
    return welcome_messages.get(character_name, welcome_messages["Guerrier"])
