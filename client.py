from factory import Factory


if __name__ =='__main__':
    inp = input('Enter mode of transportation (air/sea/road): ')
    # Method: 1 (Using if-else to decide the mode)
    obj = Factory().decide_transport_mode(inp.lower())
    if obj is not None:
        obj.run()
    else:
        print("[!] Invalid input!")
    
    # Method: 2 (Using map and getting object directly)
    normalizer = Factory().get_normalizer(inp)
    if normalizer is not None:
        normalizer().run()
    else:
        print("[!] Invalid input!")
