<h1>Liste des etudiants</h1>

<ul>
    <?php foreach ($students as $student): ?>
        <li>
            <?= $student['name'] ?> (<?= $student['age'] ?> ans)
        </li>
    <?php endforeach; ?>
</ul>