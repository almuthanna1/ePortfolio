interface ProjectCardProps {
  title: string;
  desc: string;
}

export default function ProjectCard({ title, desc }: ProjectCardProps) {
  return (
    <div className="border rounded-lg p-4 shadow-md hover:shadow-lg">
      <h3 className="font-semibold text-lg">{title}</h3>
      <p className="text-gray-600">{desc}</p>
    </div>
  );
}