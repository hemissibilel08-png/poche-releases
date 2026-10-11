# Poche pour macOS

[**Télécharger Poche.zip**](https://github.com/hemissibilel08-png/poche-releases/releases/latest/download/Poche.zip)

Un petit panier flottant pour garder vos fichiers à portée de main.

**Mac Apple Silicon · macOS 13 ou ultérieur.** Décompressez le ZIP, placez Poche.app dans Applications puis ouvrez-la. Aucun script à lancer.

Les mises à jour sont téléchargées et vérifiées automatiquement. Poche attend un moment calme pour redémarrer ; vos paniers sont conservés. Le menu de Poche permet aussi de vérifier une mise à jour ou de désactiver les mises à jour automatiques.

Installez Poche dans Applications, hors d’un dossier iCloud. Les paniers restent dans `~/Library/Application Support/Poche`, séparément de l’app. Une ancienne sauvegarde Poche-data située à côté de l’app est migrée automatiquement et conservée comme copie de secours. L'application est signée localement et n'est pas notarisée par Apple ; macOS peut demander une autorisation à la première ouverture.

Ce dépôt contient uniquement les versions compilées, le flux signé et l'automatisation de distribution. Les sources de l'application restent privées. Aucune donnée de panier n'est publiée.

Les signatures Ed25519 du ZIP et du flux sont vérifiées avant publication et dans l'application. Sparkle est inclus sous sa licence BSD ; sa licence figure dans Poche.app.
