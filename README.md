# Poche — macOS et bêta Windows

Un petit panier flottant pour garder vos fichiers à portée de main.

## Windows 11 x64 — bêta

[**Télécharger la bêta Windows**](https://github.com/hemissibilel08-png/poche-releases/releases?q=windows-v&expanded=true) — choisissez `Poche-Windows-x64.exe` dans la version la plus récente. Aucun script ni installation de .NET nécessaire.

Poches persistantes, glisser-déposer, secousse dans l’Explorateur, poignée lumineuse, rangement animé au bord, menu de notification et démarrage à la connexion. L’interface reprend les proportions compactes et le parcours Magic Links du Mac.

Pour les Magic Links, importez une fois le fichier `.poche-access` remis **en privé** par Bilel : menu de la poche → « Activer les Magic Links… ». Ne publiez pas ce fichier. Tous les testeurs Mac et Windows partagent un plafond serveur de **8 Go**, avec moins de 1 Go par envoi. Mot de passe, expiration et usage unique sont disponibles.

Cette bêta Intel/AMD n’a pas de signature Authenticode commerciale ; Windows peut afficher un avertissement de réputation. Les mises à jour sont téléchargées, authentifiées et installées automatiquement après un moment d’inactivité, avec restauration de l’ancienne version si le redémarrage échoue. Les poches et l’accès Magic Links restent conservés. Poche s’installe dans votre dossier utilisateur, sans administrateur. Les versions beta.1/beta.2 nécessitent un dernier téléchargement manuel pour activer ce mécanisme. Les tests automatisés sont exécutés sous Windows ; les gestes et les configurations à plusieurs écrans restent à éprouver sur les PC des testeurs.

## macOS

[**Télécharger Poche.zip**](https://github.com/hemissibilel08-png/poche-releases/releases/latest/download/Poche.zip)

**Mac Apple Silicon · macOS 13 ou ultérieur.** Décompressez le ZIP, placez Poche.app dans Applications puis ouvrez-la. Aucun script à lancer.

Les mises à jour sont téléchargées et vérifiées automatiquement. Poche attend un moment calme pour redémarrer ; vos paniers sont conservés. Le menu de Poche permet aussi de vérifier une mise à jour ou de désactiver les mises à jour automatiques.

Installez Poche dans Applications, hors d’un dossier iCloud. Les paniers restent dans `~/Library/Application Support/Poche`, séparément de l’app. Une ancienne sauvegarde Poche-data située à côté de l’app est migrée automatiquement et conservée comme copie de secours. L'application est signée localement et n'est pas notarisée par Apple ; macOS peut demander une autorisation à la première ouverture.

Ce dépôt contient uniquement les versions compilées, le flux signé et l'automatisation de distribution. Les sources de l'application restent privées. Aucune donnée de panier n'est publiée.

Les signatures Ed25519 du ZIP et du flux sont vérifiées avant publication et dans l'application. Sparkle est inclus sous sa licence BSD ; sa licence figure dans Poche.app.
