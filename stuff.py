 # Party Pokemon
    partyPokemon1Index = (pyboy.get_memory_value(0xD164))
    partyPokemon2Index = (pyboy.get_memory_value(0xD165))
    partyPokemon3Index = (pyboy.get_memory_value(0xD166))
    partyPokemon4Index = (pyboy.get_memory_value(0xD167))
    partyPokemon5Index = (pyboy.get_memory_value(0xD168))
    partyPokemon6Index = (pyboy.get_memory_value(0xD169))

    partyPokemon1Species = PokemonData.PokemonSpecies(partyPokemon1Index).name
    partyPokemon2Species = PokemonData.PokemonSpecies(partyPokemon2Index).name
    partyPokemon3Species = PokemonData.PokemonSpecies(partyPokemon3Index).name
    partyPokemon4Species = PokemonData.PokemonSpecies(partyPokemon4Index).name
    partyPokemon5Species = PokemonData.PokemonSpecies(partyPokemon5Index).name
    partyPokemon6Species = PokemonData.PokemonSpecies(partyPokemon6Index).name

    # Bag items
    numberOfItems = (pyboy.get_memory_value(0xD31D))
    bagItem1Index = (pyboy.get_memory_value(0xD31E))
    bagItem1Qty = (pyboy.get_memory_value(0xD31F))
    bagItem1Name = PokemonData.Items(bagItem1Index).name
    bagItem2Index = (pyboy.get_memory_value(0xD320))
    bagItem2Qty = (pyboy.get_memory_value(0xD321))
    bagItem2Name = PokemonData.Items(bagItem2Index).name
    bagItem3Index = (pyboy.get_memory_value(0xD322))
    bagItem3Qty = (pyboy.get_memory_value(0xD323))
    bagItem3Name = PokemonData.Items(bagItem3Index).name
    bagItem4Index = (pyboy.get_memory_value(0xD324))
    bagItem4Qty = (pyboy.get_memory_value(0xD325))
    bagItem4Name = PokemonData.Items(bagItem4Index).name
    bagItem5Index = (pyboy.get_memory_value(0xD326))
    bagItem5Qty = (pyboy.get_memory_value(0xD327))
    bagItem6Index = (pyboy.get_memory_value(0xD328))
    bagItem6Qty = (pyboy.get_memory_value(0xD329))
    bagItem7Index = (pyboy.get_memory_value(0xD32A))
    bagItem7Qty = (pyboy.get_memory_value(0xD32B))
    bagItem8Index = (pyboy.get_memory_value(0xD32C))
    bagItem8Qty = (pyboy.get_memory_value(0xD32D))
    bagItem9Index = (pyboy.get_memory_value(0xD32E))
    bagItem9Qty = (pyboy.get_memory_value(0xD32F))
    bagItem10Index = (pyboy.get_memory_value(0xD330))
    bagItem10Qty = (pyboy.get_memory_value(0xD331))
    bagItem11Index = (pyboy.get_memory_value(0xD332))
    bagItem11Qty = (pyboy.get_memory_value(0xD333))
    bagItem12Index = (pyboy.get_memory_value(0xD334))
    bagItem12Qty = (pyboy.get_memory_value(0xD335))
    bagItem13Index = (pyboy.get_memory_value(0xD336))
    bagItem13Qty = (pyboy.get_memory_value(0xD337))
    bagItem14Index = (pyboy.get_memory_value(0xD338))
    bagItem14Qty = (pyboy.get_memory_value(0xD339))
    bagItem15Index = (pyboy.get_memory_value(0xD33A))
    bagItem15Qty = (pyboy.get_memory_value(0xD33B))
    bagItem16Index = (pyboy.get_memory_value(0xD33C))
    bagItem16Qty = (pyboy.get_memory_value(0xD33D))
    bagItem17Index = (pyboy.get_memory_value(0xD33E))
    bagItem17Qty = (pyboy.get_memory_value(0xD33F))
    bagItem18Index = (pyboy.get_memory_value(0xD340))
    bagItem18Qty = (pyboy.get_memory_value(0xD341))
    bagItem19Index = (pyboy.get_memory_value(0xD342))
    bagItem19Qty = (pyboy.get_memory_value(0xD343))
    bagItem20Index = (pyboy.get_memory_value(0xD344))
    bagItem20Qty = (pyboy.get_memory_value(0xD345))

    # print(bagItem1Name)
    # # print(bagItem1Qty)
    # print(bagItem2Name)
    # # print(bagItem2Qty)
    # print(bagItem3Name)
    # # print(bagItem3Qty)
    # print(bagItem4Name)
    # # print(bagItem4Qty)
    # print(bagItem5Index)
    # # print(bagItem5Qty)
    # print(bagItem6Index)
    # # print(bagItem6Qty)
    # print(bagItem7Index)
    # # print(bagItem7Qty)
    # print(bagItem8Index)
    # # print(bagItem8Qty)
    # print(bagItem9Index)
    # # print(bagItem9Qty)
    # print(bagItem10Index)
    # # print(bagItem10Qty)
    # print(bagItem11Index)
    # # print(bagItem11Qty)
    # print(bagItem12Index)
    # # print(bagItem12Qty)
    # print(bagItem13Index)
    # # print(bagItem13Qty)
    # print(bagItem14Index)
    # # print(bagItem14Qty)
    # print(bagItem15Index)
    # # print(bagItem15Qty)
    # print(bagItem16Index)
    # # print(bagItem16Qty)
    # print(bagItem17Index)
    # # print(bagItem17Qty)
    # print(bagItem18Index)
    # # print(bagItem18Qty)
    # print(bagItem19Index)
    # # print(bagItem19Qty)
    # print(bagItem20Index)
    # # print(bagItem20Qty)
    
    # Battle
    # battleTurns = (pyboy.get_memory_value(0xCCD5))
    # battleType = (pyboy.get_memory_value(0xD05A))
    # playerSubstituteHp = (pyboy.get_memory_value(0xCCD7))
    # enemySubstituteHp = (pyboy.get_memory_value(0xCCD8))
    # moveMenuType = (pyboy.get_memory_value(0xCCDB))
    # playerSelectedMoveIndex = (pyboy.get_memory_value(0xCCDC))
    # playerSelectedMoveName = PokemonData.Moves(playerSelectedMoveIndex).name
    # enemySelectedMoveIndex = (pyboy.get_memory_value(0xCCDD))
    # enemySelectedMoveName = PokemonData.Moves(enemySelectedMoveIndex).name

    # print(playerSelectedMoveName)
    # print(enemySelectedMoveName)
    
    # paydayEarnings1 = (pyboy.get_memory_value(0xCCE5))
    # paydayEarnings2 = (pyboy.get_memory_value(0xCCE6))
    # paydayEarnings3 = (pyboy.get_memory_value(0xCCE7))

    # enemyMoveDisabled = (pyboy.get_memory_value(0xCCEF))
    
    # enemyPokemonID = (pyboy.get_memory_value(0xCFD8))
    # enemyPokemonSpecies = PokemonData.PokemonSpecies(enemyPokemonID).name
    # enemyPokemonCurrentHP1 = (pyboy.get_memory_value(0xCFE6))
    # enemyPokemonCurrentHP2 = (pyboy.get_memory_value(0xCFE7))
    # enemyPokemonTotalCurrentHP = (enemyPokemonCurrentHP1 + enemyPokemonCurrentHP2)
    
    # enemyPokemonMaxHP1 = (pyboy.get_memory_value(0xCFF4))
    # enemyPokemonMaxHP2 = (pyboy.get_memory_value(0xCFF5))
    # enemyPokemonTotalMaxHP = (enemyPokemonMaxHP1 + enemyPokemonMaxHP2)

    # if enemyPokemonTotalMaxHP != 0:
    #     enemyPokemonHPPercentage = (enemyPokemonTotalCurrentHP / enemyPokemonTotalMaxHP) * 100

    # if 'enemyPokemonHPPercentage' in locals():
    #     print(enemyPokemonHPPercentage)

    # enemyPokemonLevel = (pyboy.get_memory_value(0xCFF3))

    # print(enemyPokemonLevel)

    # # TODO
    # enemyPokemonStatus = (pyboy.get_memory_value(0xCFE9))

    # playerPokemonID = (pyboy.get_memory_value(0xD014))
    # playerPokemonSpecies = PokemonData.PokemonSpecies(playerPokemonID).name
    
    # print(playerPokemonSpecies)

    # playerPokemonName1 = (pyboy.get_memory_value(0xD009))
    # playerPokemonName2 = (pyboy.get_memory_value(0xD010))
    # playerPokemonName3 = (pyboy.get_memory_value(0xD011))
    # playerPokemonName4 = (pyboy.get_memory_value(0xD012))
    # playerPokemonName5 = (pyboy.get_memory_value(0xD013))


    # playerPokemonCurrentHP1 = (pyboy.get_memory_value(0xD015))
    # playerPokemonCurrentHP2 = (pyboy.get_memory_value(0xD016))
    # playerPokemonTotalCurrentHP = (playerPokemonCurrentHP1 + playerPokemonCurrentHP2)

    # print (playerPokemonTotalCurrentHP)

    # playerPokemonMaxHP1 = (pyboy.get_memory_value(0xD023))
    # playerPokemonMaxHP2 = (pyboy.get_memory_value(0xD024))
    # playerPokemonTotalMaxHP = (playerPokemonMaxHP1 + playerPokemonMaxHP2)

    # print (playerPokemonTotalMaxHP)

    # playerPokemonStatus = (pyboy.get_memory_value(0xD018))
    # playerPokemonLevel = (pyboy.get_memory_value(0xD022))
    
    # print(playerPokemonLevel)

    # playerPokemonMove1Index = (pyboy.get_memory_value(0xD01C))
    # playerPokemonMove1Name = PokemonData.Moves(playerPokemonMove1Index).name
    # playerPokemonMove2Index = (pyboy.get_memory_value(0xD01D))
    # playerPokemonMove2Name = PokemonData.Moves(playerPokemonMove2Index).name
    # playerPokemonMove3Index = (pyboy.get_memory_value(0xD01E))
    # playerPokemonMove3Name = PokemonData.Moves(playerPokemonMove3Index).name
    # playerPokemonMove4Index = (pyboy.get_memory_value(0xD01F))
    # playerPokemonMove4Name = PokemonData.Moves(playerPokemonMove4Index).name

    # print(playerPokemonMove1Name)
    # print(playerPokemonMove2Name)
    # print(playerPokemonMove3Name)
    # print(playerPokemonMove4Name)

    # playerPokemonMove1PP = (pyboy.get_memory_value(0xD02D))
    # playerPokemonMove2PP = (pyboy.get_memory_value(0xD02E))
    # playerPokemonMove3PP = (pyboy.get_memory_value(0xD02F))
    # playerPokemonMove4PP = (pyboy.get_memory_value(0xD030))

    # print(playerPokemonMove1PP)
    # print(playerPokemonMove2PP)
    # print(playerPokemonMove3PP)
    # print(playerPokemonMove4PP)

    # playerPokemonDisobedient = (pyboy.get_memory_value(0xCCED))

    # print(playerPokemonDisobedient)

    # playerMoveDisabled = (pyboy.get_memory_value(0xCCEF))

    # print(playerMoveDisabled)

    # The critical hit flag stays until you click. If it's 1, it's a critical hit. If it's 0, it's not. If it's 2, it's a OHKO.
    # criticalHit = (pyboy.get_memory_value(0xD05E))
    # print(criticalHit)

    # battleStatus = (pyboy.get_memory_value(0xD062))
    # print(battleStatus)

    # time.sleep(1)