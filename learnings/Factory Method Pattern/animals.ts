import { Injectable, Controller, Get, Post, Delete, Put, Param, Body } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Animal } from './animal.entity';

// Interfaces
interface AnimalDto {
  id: string;
  type: AnimalType;
  name: string;
  age: number;
}

// Step 0: Create an enumeration for animal types
enum AnimalType {
  DOG = 'Dog',
  CAT = 'Cat',
  FISH = 'Fish',
}

// Step 1: Create a base animal service interface
interface BaseAnimalService {
  create(data: AnimalDto): Promise<AnimalDto>;
  read(id: string): Promise<AnimalDto | null>;
  update(id: string, data: Partial<AnimalDto>): Promise<AnimalDto | null>;
  delete(id: string): Promise<boolean>;
  list(): Promise<AnimalDto[]>;
}

// Step 2: Create concrete service implementations for each animal type
@Injectable()
class DogService implements BaseAnimalService {
  constructor(
    @InjectRepository(Animal)
    private animalRepository: Repository<Animal>
  ) {}

  async create(data: AnimalDto): Promise<AnimalDto> {
    console.log('Creating a dog with custom logic');
    return this.animalRepository.save(data);
  }

  async read(id: string): Promise<AnimalDto | null> {
    return this.animalRepository.findOne({ where: { id, type: AnimalType.DOG } });
  }

  async update(id: string, data: Partial<AnimalDto>): Promise<AnimalDto | null> {
    await this.animalRepository.update({ id, type: AnimalType.DOG }, data);
    return this.read(id);
  }

  async delete(id: string): Promise<boolean> {
    const result = await this.animalRepository.delete({ id, type: AnimalType.DOG });
    return result.affected > 0;
  }

  async list(): Promise<AnimalDto[]> {
    return this.animalRepository.find({ where: { type: AnimalType.DOG } });
  }
}

@Injectable()
class CatService implements BaseAnimalService {
  constructor(
    @InjectRepository(Animal)
    private animalRepository: Repository<Animal>
  ) {}

  async create(data: AnimalDto): Promise<AnimalDto> {
    console.log('Creating a cat with API call');
    await new Promise(resolve => setTimeout(resolve, 1000));
    return this.animalRepository.save(data);
  }

  async read(id: string): Promise<AnimalDto | null> {
    return this.animalRepository.findOne({ where: { id, type: AnimalType.DOG } });
  }

  async update(id: string, data: Partial<AnimalDto>): Promise<AnimalDto | null> {
    await this.animalRepository.update({ id, type: AnimalType.DOG }, data);
    return this.read(id);
  }

  async delete(id: string): Promise<boolean> {
    const result = await this.animalRepository.delete({ id, type: AnimalType.DOG });
    return result.affected > 0;
  }

  async list(): Promise<AnimalDto[]> {
    return this.animalRepository.find({ where: { type: AnimalType.DOG } });
  }
}

@Injectable()
class FishService implements BaseAnimalService {
  constructor(
    @InjectRepository(Animal)
    private animalRepository: Repository<Animal>
  ) {}

  async create(data: AnimalDto): Promise<AnimalDto> {
    return this.animalRepository.save(data);
  }

  async read(id: string): Promise<AnimalDto | null> {
    return this.animalRepository.findOne({ where: { id, type: AnimalType.DOG } });
  }

  async update(id: string, data: Partial<AnimalDto>): Promise<AnimalDto | null> {
    await this.animalRepository.update({ id, type: AnimalType.DOG }, data);
    return this.read(id);
  }

  async delete(id: string): Promise<boolean> {
    const result = await this.animalRepository.delete({ id, type: AnimalType.DOG });
    return result.affected > 0;
  }

  async list(): Promise<AnimalDto[]> {
    return this.animalRepository.find({ where: { type: AnimalType.DOG } });
  }
}


@Injectable()
class AnimalServiceFactory {
  constructor(
    private dogService: DogService,
    private catService: CatService,
    private fishService: FishService
  ) {}

  getService(type: AnimalType): BaseAnimalService {
    switch (type) {
      case AnimalType.DOG:
        return this.dogService;
      case AnimalType.CAT:
        return this.catService;
      case AnimalType.FISH:
        return this.fishService;
      default:
        throw new Error('Invalid Animal Type');
    }
  }
}


@Injectable()
export class AnimalService {
  constructor(private serviceFactory: AnimalServiceFactory) {}

  async create(type: AnimalType, data: AnimalDto): Promise<AnimalDto> {
    const service = this.serviceFactory.getService(type);
    return service.create({ ...data, type });
  }

  async read(type: AnimalType, id: string): Promise<AnimalDto | null> {
    const service = this.serviceFactory.getService(type);
    return service.read(id);
  }

  async update(type: AnimalType, id: string, data: Partial<AnimalDto>): Promise<AnimalDto | null> {
    const service = this.serviceFactory.getService(type);
    return service.update(id, data);
  }

  async delete(type: AnimalType, id: string): Promise<boolean> {
    const service = this.serviceFactory.getService(type);
    return service.delete(id);
  }

  async list(type: AnimalType): Promise<AnimalDto[]> {
    const service = this.serviceFactory.getService(type);
    return service.list();
  }
}



@Controller('animals')
export class AnimalController {
  constructor(private animalService: AnimalService) {}

  @Post(':type')
  create(@Param('type') type: AnimalType, @Body() data: AnimalDto) {
    return this.animalService.create(type, data);
  }

  @Get(':type/:id')
  read(@Param('type') type: AnimalType, @Param('id') id: string) {
    return this.animalService.read(type, id);
  }

  @Put(':type/:id')
  update(@Param('type') type: AnimalType, @Param('id') id: string, @Body() data: Partial<AnimalDto>) {
    return this.animalService.update(type, id, data);
  }

  @Delete(':type/:id')
  delete(@Param('type') type: AnimalType, @Param('id') id: string) {
    return this.animalService.delete(type, id);
  }

  @Get(':type')
  list(@Param('type') type: AnimalType) {
    return this.animalService.list(type);
  }
}